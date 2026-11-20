"""Testes do kit IA sem estrago. Rodar: python3 -m unittest discover -s tests -v"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HOOK = RAIZ / "kit/.claude/hooks/pronto.sh"
sys.path.insert(0, str(RAIZ / "ferramentas"))
import conferir as cv  # noqa: E402


def rodar_hook(projeto, cmd, extra_env=None):
    env = {**os.environ, "CLAUDE_PROJECT_DIR": str(projeto), "PRONTO_CMD": cmd, **(extra_env or {})}
    return subprocess.run(["bash", str(HOOK)], input='{"stop_hook_active": false}', env=env,
                          capture_output=True, text=True)


class Hook(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.p = Path(self.tmp.name)
        (self.p / ".claude").mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def test_checagem_falha_sai_com_2_e_explica(self):
        r = rodar_hook(self.p, "echo teste quebrou; false")
        self.assertEqual(r.returncode, 2)
        self.assertIn("Ainda não está pronto", r.stderr)
        self.assertIn("teste quebrou", r.stderr)

    def test_checagem_passa_sai_com_0(self):
        self.assertEqual(rodar_hook(self.p, "true").returncode, 0)

    def test_para_de_bloquear_depois_do_maximo(self):
        codigos = [rodar_hook(self.p, "false", {"PRONTO_MAX": "2"}).returncode for _ in range(3)]
        self.assertEqual(codigos, [2, 2, 1])
        self.assertFalse((self.p / ".claude/.pronto-bloqueios").exists())

    def test_sucesso_zera_a_contagem(self):
        rodar_hook(self.p, "false")
        rodar_hook(self.p, "true")
        self.assertFalse((self.p / ".claude/.pronto-bloqueios").exists())

    def test_sem_checagem_nao_bloqueia(self):
        env = {**os.environ, "CLAUDE_PROJECT_DIR": str(self.p)}
        env.pop("PRONTO_CMD", None)
        r = subprocess.run(["bash", str(HOOK)], input="{}", env=env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0)

    def test_comando_do_arquivo_pronto_cmd(self):
        (self.p / ".claude/pronto.cmd").write_text("false\n")
        env = {**os.environ, "CLAUDE_PROJECT_DIR": str(self.p)}
        env.pop("PRONTO_CMD", None)
        r = subprocess.run(["bash", str(HOOK)], input="{}", env=env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)


class Exemplo(unittest.TestCase):
    def test_tres_versoes_do_login(self):
        saida = subprocess.run(["bash", str(RAIZ / "exemplo/rodar.sh")], capture_output=True, text=True).stdout
        self.assertIn("esqueceu: saída 2", saida)
        self.assertIn("deslogou: saída 2", saida)
        self.assertIn("certo: saída 0", saida)


class Conferidor(unittest.TestCase):
    def test_kit_passa(self):
        self.assertEqual([a for a in cv.conferir(RAIZ / "kit") if a[0] == "falha"], [])

    def test_settings_do_kit_e_json_valido_com_chaves_oficiais(self):
        s = json.loads((RAIZ / "kit/.claude/settings.json").read_text())
        self.assertTrue(s["sandbox"]["enabled"])
        self.assertIn("Stop", s["hooks"])
        self.assertIn("TaskCompleted", s["hooks"])
        deny = s["permissions"]["deny"]
        for regra in ["Read(./.env)", "Read(./.env.*)", "Read(./secrets/**)", "Read(~/.ssh/**)", "Bash(rm -rf *)"]:
            self.assertIn(regra, deny)

    def test_exemplos_sao_json_com_chaves_oficiais(self):
        con = json.loads((RAIZ / "kit/exemplos/conectores.json").read_text())
        self.assertTrue(all(r.startswith("mcp__") for r in con["permissions"]["ask"]))
        txt = json.loads((RAIZ / "kit/exemplos/pronto-texto.json").read_text())
        h = txt["hooks"]["Stop"][0]["hooks"][0]
        self.assertEqual(h["type"], "agent")
        self.assertIn("$ARGUMENTS", h["prompt"])
        self.assertIn('"ok": false', h["prompt"])

    def test_projeto_ruim_reprova_nas_tres_trocas(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            (p / ".claude/hooks").mkdir(parents=True)
            (p / "CLAUDE.md").write_text("IMPORTANTE: NUNCA esqueça os testes\nok\n")
            (p / ".claude/hooks/teste.sh").write_text("#!/bin/bash\nnpm test || exit 1\n")
            (p / ".claude/hooks/lint.sh").write_text("#!/bin/bash\nlint || exit 2\n")
            (p / ".claude/settings.json").write_text(json.dumps({
                "permissions": {"deny": ["Read(./.env)"]},
                "hooks": {"Stop": [{"hooks": [{"type": "command", "command": ".claude/hooks/teste.sh"}]}],
                          "PostToolUse": [{"hooks": [{"type": "command", "command": ".claude/hooks/lint.sh"}]}]}}))
            achados = cv.conferir(p)
            textos = " | ".join(x for _, _, x in achados)
            self.assertEqual({t for _, t, _ in achados}, {1, 2, 3})
            self.assertIn("saída 1", textos)
            self.assertIn("sandbox desligado", textos)
            self.assertIn("PostToolUse não bloqueia", textos)
            self.assertNotIn("segredo .env", textos)
            self.assertEqual(cv.main(["x", str(p)]), 1)

    def test_sem_hook_de_parada(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            (p / ".claude").mkdir()
            (p / ".claude/settings.json").write_text("{}")
            self.assertTrue(any("Stop ou TaskCompleted" in x for _, _, x in cv.conferir(p)))


if __name__ == "__main__":
    unittest.main()
