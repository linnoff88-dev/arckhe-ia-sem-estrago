# ðŸ›¡ï¸ IA sem estrago

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

[![IA sem estrago](guia/assets/banner.jpg)](https://inematds.github.io/ia-sem-estrago/guia/)

**A IA trabalha sozinha e nÃ£o estraga o que nÃ£o tem volta.** Baseado na documentaÃ§Ã£o oficial do Claude Code e nas recomendaÃ§Ãµes dos engenheiros da Anthropic. VocÃª pede a tarefa e vai fazer outra coisa. Quando volta, ela estÃ¡ feita e testada. Nenhuma pasta foi apagada, nenhuma senha foi lida, e o Claude nÃ£o disse "pronto" antes da hora.

## ðŸ“– Guia

Para entender o que o kit faz e como ele muda o seu dia (sem parte tÃ©cnica): **https://inematds.github.io/ia-sem-estrago/guia/**

ðŸŽ¬ VÃ­deo (quem jÃ¡ usa o Claude Code): https://www.youtube.com/watch?v=uBUpckFw1Xg  
ðŸŽ¬ VÃ­deo (quem estÃ¡ comeÃ§ando): https://www.youtube.com/watch?v=JBiVZj8z-Ms

## O que Ã©

O kit pÃµe duas proteÃ§Ãµes no Claude Code:

- **A trava:** barra o que nÃ£o tem volta (apagar uma pasta inteira, ler senhas, apagar o histÃ³rico do projeto), em qualquer modo, mesmo que a IA tente. A regra para decidir Ã© uma pergunta sÃ³: *"se a IA errar isso uma vez, dÃ¡ para voltar atrÃ¡s?"*
- **O teste antes do "pronto":** vocÃª diz uma vez o que Ã© "pronto", e um teste confere isso toda vez que a IA tenta encerrar. Se falhar, ela volta e conserta.

Com as duas, vocÃª pode desligar o "permitir" e sair de perto. Tudo o que tem volta segue sozinho, no modo automÃ¡tico do Claude Code.

## Baseado na Anthropic

Nada aqui Ã© invenÃ§Ã£o nossa. O kit junta, pronto para usar, o que a Anthropic (a empresa que faz o Claude) publica e recomenda:

- **Os engenheiros do Claude Code:** na palestra "Rethinking Claude Code Best Practices", Lydia Hallie, do time do Claude Code, mostra como eles trabalham: param de vigiar, travam o que nÃ£o tem volta e cobram o "pronto" com teste. Assim passaram de 2.500 para mais de 30.000 mudanÃ§as de cÃ³digo por dia. [Assistir](https://www.youtube.com/watch?v=vlfCjWuv4es)
- **O cansaÃ§o de aprovar:** quem aprova tudo Ã  mÃ£o acaba aceitando 93% dos pedidos; o registro interno da Anthropic tem casos reais de IA apagando ramos do git, enviando uma chave de acesso para fora e mexendo no banco de produÃ§Ã£o. [Artigo: How we built Claude Code auto mode](https://www.anthropic.com/research/claude-code-auto-mode)
- **A caixa fechada (sandbox):** reduziu os pedidos de permissÃ£o em 84%, com mais seguranÃ§a. [Artigo: Making Claude Code safer with sandboxing](https://www.anthropic.com/research/claude-code-sandboxing)
- **Cada peÃ§a na documentaÃ§Ã£o oficial:** a trava = [PermissÃµes](https://code.claude.com/docs/en/permissions); a caixa fechada = [Sandbox](https://code.claude.com/docs/en/sandboxing); o teste antes do "pronto" = [Hooks](https://code.claude.com/docs/en/hooks); o jeito de pedir = [Boas prÃ¡ticas](https://code.claude.com/docs/en/best-practices). Conferido em 17/11/2026.

Os 14% (pessoas que aprovam um por um) e 89% (modo automÃ¡tico) foram mostrados na palestra; os 93% e 84% estÃ£o nos artigos oficiais.

## Como comeÃ§ar (sem ser tÃ©cnico)

Abra o Claude Code, ou o Codex, na pasta do seu projeto e cole:

```text
Leia o kit "IA sem estrago" em https://github.com/inematds/ia-sem-estrago (o README explica tudo, inclusive a instalaÃ§Ã£o).
Depois olhe este projeto e me responda em portuguÃªs simples:
1. O que aqui nÃ£o teria volta se vocÃª errasse (apagar, senhas, enviar algo para fora)?
2. Qual teste ou conferÃªncia prova que uma tarefa ficou pronta neste projeto?
3. Quais partes do kit valem a pena para mim, e quais nÃ£o?
NÃ£o mude nada ainda. Mostre o plano e espere eu dizer sim.
```

A IA mostra o plano, vocÃª aprova o que quiser e ela instala sÃ³ isso. O kit Ã© montado para o Claude Code; o Codex tambÃ©m consegue ler e dizer se ele serve para o seu projeto.

## E se eu abro o Claude sem restriÃ§Ã£o?

Muita gente abre o Claude Code assim:

```bash
claude --chrome --dangerously-skip-permissions --exclude-dynamic-system-prompt-sections "$@"
```

**O kit continua valendo.** Testamos em 17/11/2026, no Claude Code 2.1.327, com `--dangerously-skip-permissions`:

| O que pedimos | O que aconteceu |
|---|---|
| ler o `.env` | **negado** pela trava (`Read(./.env)`) |
| `rm -rf lixo` | **negado** pela trava; a pasta ficou lÃ¡ |
| dizer "pronto" com a checagem falhando | o hook barrou 3 vezes e depois soltou (`PRONTO_MAX`) |
| usar uma ferramenta com regra `ask` | **pediu confirmaÃ§Ã£o** mesmo nesse modo (no `-p`, vira recusa) |

O que muda Ã© outra coisa: sem restriÃ§Ã£o, **o porteiro do modo automÃ¡tico sai**. No modo `auto`, um segundo modelo olha cada aÃ§Ã£o que nÃ£o estÃ¡ na trava e barra o que parece estrago ou envio para fora. Com `--dangerously-skip-permissions`, tudo o que nÃ£o estÃ¡ na trava passa direto. Por isso:

- **Prefira `claude --permission-mode auto`** (Ã© o padrÃ£o desde a 2.1.283). VocÃª tem o mesmo "nÃ£o pede licenÃ§a" e ainda o porteiro.
- **Se for usar sem restriÃ§Ã£o**, a trava do kit Ã© a Ãºnica coisa entre a IA e o estrago: confira que ela estÃ¡ no projeto (`python3 ferramentas/conferir.py .`). A Anthropic recomenda esse modo sÃ³ em contÃªiner ou mÃ¡quina virtual.
- **`--chrome` abre o navegador**, e o navegador fica fora da caixa fechada (o sandbox sÃ³ cerca comandos do terminal). Ponha regra `ask` nos conectores e no navegador (`kit/exemplos/conectores.json`).
- `--exclude-dynamic-system-prompt-sections` sÃ³ mexe no texto de sistema; nÃ£o muda nenhuma proteÃ§Ã£o.

---

## InstalaÃ§Ã£o tÃ©cnica

Para quem prefere instalar Ã  mÃ£o. Tudo Ã© texto simples para copiar; nada instala sozinho.

### PrÃ©-requisitos

- **Claude Code** com o seu projeto aberto (`claude --version`). Provado na versÃ£o 2.1.326; `/auto-mode-setup`, `/sandbox` e `/doctor prompt-audit` foram usados nessa versÃ£o.
- **Python 3 e git**, para o conferidor, os testes e para baixar o kit.
- **Sandbox no Linux/WSL2:** precisa de `bubblewrap` e `socat` (`sudo apt install bubblewrap socat`). No macOS nÃ£o precisa instalar nada.

### Os arquivos

| Arquivo | Para quÃª |
|---|---|
| `kit/.claude/settings.json` | regras de bloqueio (`.env`, `~/.ssh`, push forÃ§ado, `rm -rf`, `reset --hard`), sandbox ligado, hooks `Stop` e `TaskCompleted` |
| `kit/.claude/hooks/pronto.sh` | roda a checagem; falhou â†’ saÃ­da 2 com o motivo; no mÃ¡ximo 3 voltas seguidas |
| `kit/teste-do-desfazer.md` | a pergunta que decide o que vai para a lista de bloqueio |
| `kit/como-e-pronto.md` | modelo de pedido com "pronto Ã©â€¦" e checagem por tarefa |
| `kit/CLAUDE.md.exemplo` | CLAUDE.md enxuto, sem IMPORTANTE em maiÃºscula |
| `kit/exemplos/pronto-texto.json` | "pronto" para texto: hook `Stop` do tipo `agent` que confere fonte de cada afirmaÃ§Ã£o e nÃºmero contra `dados.csv` |
| `kit/exemplos/conectores.json` | regras `ask` para conectores e navegador (enviar, apagar, lixeira, remover, publicar) |
| `ferramentas/conferir.py` | confere um projeto (CLAUDE.md, bloqueio + sandbox, hook do pronto); sÃ³ lÃª |
| `exemplo/` | um login nas trÃªs versÃµes (esqueceu a API velha, deslogou todo mundo, certo) + `PROVA.md` com o hook rodando de verdade |
| `guia/` | a pÃ¡gina do guia em PT, EN e ES (GitHub Pages) |

### Como funciona

`Pedido com "pronto Ã©â€¦"` â†’ `Claude trabalha no auto mode` â†’ `bloqueio + sandbox barram o que nÃ£o tem volta` â†’ `Claude tenta parar` â†’ `hook roda a checagem` â†’ `falhou: sai com 2 e volta Â· passou: pronto`

- **Ordem das permissÃµes:** `deny` (bloqueia), `ask` (pergunta), `allow` (libera). O Claude Code confere `deny` primeiro, antes do verificador do auto mode, em todos os modos, inclusive `bypassPermissions`.
- **A regra olha o texto do comando**, nÃ£o o efeito. Por isso o kit liga tambÃ©m o **sandbox**, em que o comando sÃ³ lÃª as pastas e sÃ³ fala com os sites liberados (`github.com`, `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org`). Se o seu projeto fala com outro site, acrescente o domÃ­nio em `sandbox.network.allowedDomains`.
- **Por que `Stop` e `TaskCompleted`:** sÃ£o os momentos em que o Claude tenta parar ou fechar uma tarefa. `PostToolUse` nÃ£o bloqueia nem com 2, porque a ferramenta jÃ¡ rodou.
- **SaÃ­da 2, nÃ£o 1:** com 2, o Claude Code devolve o erro ao Claude, que volta e conserta. Com 1, sÃ³ mostra o erro e o Claude segue como se estivesse feito.
- **ProteÃ§Ã£o contra laÃ§o:** o `pronto.sh` bloqueia no mÃ¡ximo 3 vezes seguidas (`PRONTO_MAX`) e depois deixa parar para vocÃª olhar.
- **Conectores e navegador** (Gmail, Drive, Slack, `--chrome`): as ferramentas se chamam `mcp__<servidor>__<aÃ§Ã£o>` (veja os nomes em `/mcp`). O kit sugere `ask`, nÃ£o `deny`: `ask` continua pedindo confirmaÃ§Ã£o em todo modo, inclusive `--dangerously-skip-permissions`, e vocÃª ainda consegue mandar o e-mail quando quiser. Para proibir de vez, mova a regra para `deny`. O `*` vale em qualquer parte do nome (`mcp__*__*send*`).
- **A caixa fechada sÃ³ cerca comandos do terminal.** As ferramentas Read/Edit e os conectores ficam fora dela; por isso a trava repete `~/.ssh`, `.env` e `secrets/`. No Linux, se aparecer `Sandbox disabled: ... socat not installed`, o sandbox **nÃ£o estÃ¡ ligado**: instale `bubblewrap` e `socat`.
- **O modo automÃ¡tico deixa ler o `.env` e mandar a senha para a API dela** (Ã© o padrÃ£o da Anthropic). Quem quer que a IA nunca veja a senha precisa da trava `Read(./.env)`, que o kit jÃ¡ pÃµe.
- **Diga ao modo automÃ¡tico o que Ã© seu.** O porteiro trata como "de fora" tudo o que nÃ£o conhece. Liste os seus repositÃ³rios, buckets e domÃ­nios em `autoMode.environment`, **em `~/.claude/settings.json`** (o Claude Code ignora `autoMode` em `.claude/settings.json` do projeto, para um repositÃ³rio nÃ£o se autoliberar):
  ```json
  { "autoMode": { "environment": ["$defaults", "Source control: github.com/minha-org e todos os repos dela"] } }
  ```
  `$defaults` mantÃ©m as regras da Anthropic; `/auto-mode-setup` escreve isso para vocÃª e `claude auto-mode config` mostra o resultado.
- **Limite do prÃ³prio Claude Code:** depois de 8 bloqueios seguidos de hook `Stop`, ele encerra sozinho (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`). O `pronto.sh` para em 3, antes disso.
- **De onde vem a checagem**, nesta ordem: a variÃ¡vel `PRONTO_CMD`, o arquivo `.claude/pronto.cmd` (uma linha) ou a detecÃ§Ã£o de `npm test` / `python3 -m unittest`. Sem nada para checar, nÃ£o bloqueia. Se juntar um `grep`, confira que a pasta existe: `! grep -rn "x" src/` passa sempre quando nÃ£o hÃ¡ `src/`.

## O processo, do inÃ­cio ao fim

Troque `~/meu-projeto` pela pasta do seu projeto. âš™ï¸ = script Â· ðŸ§  = vocÃª (Ã s vezes com o Claude).

| # | Passo | Comando | Quem |
|---|---|---|---|
| 0 | Baixar o kit | `git clone https://github.com/inematds/ia-sem-estrago.git && cd ia-sem-estrago` | ðŸ§  vocÃª |
| 1 | Conferir o seu projeto (falhas na 1Âª vez sÃ£o normais) | `python3 ferramentas/conferir.py ~/meu-projeto` | âš™ï¸ script |
| 2 | Copiar a configuraÃ§Ã£o e o hook | `cp -rn kit/.claude ~/meu-projeto/` e `echo ".claude/.pronto-bloqueios" >> ~/meu-projeto/.gitignore` (o `-n` nÃ£o sobrescreve; se jÃ¡ houver `settings.json`, junte as chaves Ã  mÃ£o) | ðŸ§  vocÃª |
| 3 | Dizer qual Ã© a checagem de "pronto" (texto: junte `kit/exemplos/pronto-texto.json`) | `echo "python3 -m unittest discover -s tests -q" > ~/meu-projeto/.claude/pronto.cmd` (troque pelo teste do seu projeto) | ðŸ§  vocÃª |
| 4 | Ligar o auto mode e descrever a sua casa | `claude --permission-mode auto` (ou Shift+Tab atÃ© "âµâµ auto mode on"; padrÃ£o desde a 2.1.283), depois `/auto-mode-setup` | ðŸ§  vocÃª + Claude |
| 5 | Ligar e testar o sandbox; se usa conectores ou `--chrome`, juntar `kit/exemplos/conectores.json` | `/sandbox` | ðŸ§  vocÃª |
| 6 | Enxugar o CLAUDE.md | `/doctor prompt-audit` e, em cada linha, "ele descobriria isso lendo o cÃ³digo?" | ðŸ§  vocÃª + Claude |
| 7 | Ver o hook cobrar | `bash exemplo/rodar.sh` (esqueceu: 2 Â· deslogou: 2 Â· certo: 0) | âš™ï¸ script |
| 8 | Conferir de novo | passo 1 â†’ `ia sem estrago: ok` | âš™ï¸ script |

O conferidor lÃª os arquivos; ele nÃ£o sabe se vocÃª rodou os passos 4 e 5 dentro do Claude Code.

## Testes

```bash
python3 -m unittest discover -s tests -v   # 12 testes, sÃ³ Python 3
bash exemplo/rodar.sh                       # esqueceu: 2 Â· deslogou: 2 Â· certo: 0
```

## A prova

O hook rodou de verdade no Claude Code 2.1.326, pela assinatura, em 17/11/2026. Com um erro escondido (a soma subtraÃ­a), o Claude disse "pronto"; o hook rodou o teste, viu a falha e saiu com 2; o Claude voltou, achou o erro, consertou e sÃ³ entÃ£o parou. Registro: `exemplo/PROVA.md`.

## De onde vem

Palestra "Rethinking Claude Code Best Practices", de Lydia Hallie (time do Claude Code, Anthropic, AI Engineer): https://www.youtube.com/watch?v=vlfCjWuv4es. Sintaxe conferida na documentaÃ§Ã£o oficial do Claude Code (permissions, sandboxing, hooks, auto mode) em 17/11/2026. O estudo dos 14% e 89% foi sÃ³ mostrado na palestra. Resumo de terceiros da mesma palestra, que inspirou a trava de conectores e o "pronto" de texto: "Anthropic Engineer Explains: The New Way to Use Claude Code", de Nate Herk (PDF); conferimos cada item na documentaÃ§Ã£o antes de pÃ´r no kit.

GrÃ¡tis no [inema.club](https://inema.club), direto na internet. LicenÃ§a MIT.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>