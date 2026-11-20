#!/usr/bin/env python3
"""conferir.py — confere se um projeto do Claude Code está "IA sem estrago".

Uso: python3 ferramentas/conferir.py <pasta-do-projeto> [--json]

Lê <pasta>/.claude/settings.json (e settings.local.json, se houver) e <pasta>/CLAUDE.md e confere:
  troca 1 — CLAUDE.md sem gritos (IMPORTANTE/NUNCA/NEVER/ALWAYS em maiúscula) e enxuto
  troca 2 — regras de bloqueio do teste do desfazer (.env, ~/.ssh, push --force, rm -rf) e sandbox ligado
  troca 3 — hook de Stop/TaskCompleted que cobra "pronto"; script que falha com saída 1 (não bloqueia)
            ou hook de "pronto" em PostToolUse (não bloqueia)

Só lê arquivos; não muda nada. Sai 0 se não houver falha, 1 se houver.
"""
import json
import re
import sys
from pathlib import Path

GRITOS = re.compile(r"\b(IMPORTANTE|IMPORTANT|NUNCA|NEVER|ALWAYS|SEMPRE|CRITICAL|CRÍTICO|MUST)\b")
ESSENCIAIS = {
    "segredo .env": re.compile(r"^Read\((\./)?\.env"),
    "chaves ~/.ssh": re.compile(r"^Read\(~/\.ssh"),
    "push forçado": re.compile(r"^Bash\(git push (--force|-f)"),
    "apagar tudo (rm -rf)": re.compile(r"^Bash\(rm -rf"),
}
LIMITE_LINHAS = 120


def ler_settings(pasta):
    junto = {}
    for nome in ("settings.json", "settings.local.json"):
        p = pasta / ".claude" / nome
        if p.exists():
            try:
                d = json.loads(p.read_text())
            except ValueError as e:
                raise SystemExit(f"erro: {p} não é JSON válido: {e}")
            for k, v in d.items():
                if isinstance(v, dict) and isinstance(junto.get(k), dict):
                    junto[k] = {**junto[k], **v}
                else:
                    junto[k] = v
    return junto


def scripts_do_hook(entradas, pasta):
    for grupo in entradas or []:
        for h in grupo.get("hooks", []):
            cmd = h.get("command", "")
            for parte in re.findall(r"[\w$\"{}./-]+\.(?:sh|py)", cmd):
                limpo = re.sub(r'["{}]', "", parte).replace("$CLAUDE_PROJECT_DIR", str(pasta))
                yield cmd, Path(limpo) if limpo.startswith("/") else pasta / limpo


def sai_so_com_1(script):
    """True se o script falha com 'exit 1' e nunca usa 'exit 2' (não manda o Claude voltar)."""
    try:
        t = script.read_text()
    except OSError:
        return False
    return bool(re.search(r"\bexit 1\b|sys\.exit\(1\)", t)) and not re.search(r"\bexit 2\b|sys\.exit\(2\)", t)


def conferir(pasta):
    pasta = Path(pasta).resolve()
    achados = []  # (nivel, troca, texto)
    s = ler_settings(pasta)

    claude_md = pasta / "CLAUDE.md"
    if claude_md.exists():
        linhas = claude_md.read_text().splitlines()
        gritos = [i + 1 for i, l in enumerate(linhas) if GRITOS.search(l)]
        if gritos:
            achados.append(("aviso", 1, f"CLAUDE.md tem {len(gritos)} linha(s) gritando (linhas {gritos[:8]}): "
                            "nos modelos de hoje isso atrapalha; diga com calma ou apague"))
        if len(linhas) > LIMITE_LINHAS:
            achados.append(("aviso", 1, f"CLAUDE.md com {len(linhas)} linhas: para cada uma, o Claude descobriria "
                            "isso lendo o código? Rode /doctor prompt-audit"))

    deny = (s.get("permissions") or {}).get("deny") or []
    for nome, padrao in ESSENCIAIS.items():
        if not any(padrao.search(r) for r in deny):
            achados.append(("falha", 2, f"sem regra de bloqueio para {nome} (não tem volta: vai em permissions.deny)"))
    if not (s.get("sandbox") or {}).get("enabled"):
        achados.append(("falha", 2, "sandbox desligado: regra de bloqueio vê o texto do comando, não o que ele faz "
                        "(ligue com /sandbox ou sandbox.enabled)"))

    hooks = s.get("hooks") or {}
    cobra = [e for e in ("Stop", "TaskCompleted") if hooks.get(e)]
    if not cobra:
        achados.append(("falha", 3, "nenhum hook de Stop ou TaskCompleted: ninguém cobra 'pronto' antes de parar"))
    for evento in ("Stop", "TaskCompleted", "SubagentStop"):
        for cmd, script in scripts_do_hook(hooks.get(evento), pasta):
            if not script.exists():
                achados.append(("falha", 3, f"hook {evento} aponta para script inexistente: {script}"))
            elif sai_so_com_1(script):
                achados.append(("falha", 3, f"{script.name} ({evento}) falha com saída 1: o Claude segue como se "
                                "estivesse feito; use exit 2"))
    for cmd, script in scripts_do_hook(hooks.get("PostToolUse"), pasta):
        if script.exists() and re.search(r"\bexit 2\b", script.read_text()):
            achados.append(("aviso", 3, f"{script.name} em PostToolUse sai com 2, mas PostToolUse não bloqueia "
                            "(a ferramenta já rodou); para cobrar pronto use Stop/TaskCompleted"))
    return achados


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    achados = conferir(argv[1])
    if "--json" in argv:
        print(json.dumps([{"nivel": n, "troca": t, "texto": x} for n, t, x in achados], ensure_ascii=False, indent=1))
    else:
        for n, t, x in achados:
            print(f"[{n}] troca {t} de 3: {x}")
        falhas = sum(1 for n, *_ in achados if n == "falha")
        print("ia sem estrago: ok" if not falhas else f"ia sem estrago: {falhas} falha(s)")
    return 1 if any(n == "falha" for n, *_ in achados) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
