# ê°Å¸âºÂ¡ê¯Â¸Â IA sem estrago

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

[![IA sem estrago](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**A IA trabalha sozinha e nêÂ£o estraga o que nêÂ£o tem volta.** Baseado na documentaêÂ§êÂ£o oficial do Claude Code e nas recomendaêÂ§êÂµes dos engenheiros da Anthropic. VocêÂª pede a tarefa e vai fazer outra coisa. Quando volta, ela estêÂ¡ feita e testada. Nenhuma pasta foi apagada, nenhuma senha foi lida, e o Claude nêÂ£o disse "pronto" antes da hora.

## ê°Å¸ââ Guia

Para entender o que o kit faz e como ele muda o seu dia (sem parte têÂ©cnica): **https://linnoff88-dev.github.io/

ê°Å¸Å½Â¬ VêÂ­deo (quem jêÂ¡ usa o Claude Code): https://www.youtube.com/watch?v=uBUpckFw1Xg  
ê°Å¸Å½Â¬ VêÂ­deo (quem estêÂ¡ comeêÂ§ando): https://www.youtube.com/watch?v=JBiVZj8z-Ms

## O que êÂ©

O kit pêÂµe duas proteêÂ§êÂµes no Claude Code:

- **A trava:** barra o que nêÂ£o tem volta (apagar uma pasta inteira, ler senhas, apagar o histêÂ³rico do projeto), em qualquer modo, mesmo que a IA tente. A regra para decidir êÂ© uma pergunta sêÂ³: *"se a IA errar isso uma vez, dêÂ¡ para voltar atrêÂ¡s?"*
- **O teste antes do "pronto":** vocêÂª diz uma vez o que êÂ© "pronto", e um teste confere isso toda vez que a IA tenta encerrar. Se falhar, ela volta e conserta.

Com as duas, vocêÂª pode desligar o "permitir" e sair de perto. Tudo o que tem volta segue sozinho, no modo automêÂ¡tico do Claude Code.

## Baseado na Anthropic

Nada aqui êÂ© invenêÂ§êÂ£o nossa. O kit junta, pronto para usar, o que a Anthropic (a empresa que faz o Claude) publica e recomenda:

- **Os engenheiros do Claude Code:** na palestra "Rethinking Claude Code Best Practices", Lydia Hallie, do time do Claude Code, mostra como eles trabalham: param de vigiar, travam o que nêÂ£o tem volta e cobram o "pronto" com teste. Assim passaram de 2.500 para mais de 30.000 mudanêÂ§as de cêÂ³digo por dia. [Assistir](https://www.youtube.com/watch?v=vlfCjWuv4es)
- **O cansaêÂ§o de aprovar:** quem aprova tudo êÂ  mêÂ£o acaba aceitando 93% dos pedidos; o registro interno da Anthropic tem casos reais de IA apagando ramos do git, enviando uma chave de acesso para fora e mexendo no banco de produêÂ§êÂ£o. [Artigo: How we built Claude Code auto mode](https://www.anthropic.com/research/claude-code-auto-mode)
- **A caixa fechada (sandbox):** reduziu os pedidos de permissêÂ£o em 84%, com mais seguranêÂ§a. [Artigo: Making Claude Code safer with sandboxing](https://www.anthropic.com/research/claude-code-sandboxing)
- **Cada peêÂ§a na documentaêÂ§êÂ£o oficial:** a trava = [PermissêÂµes](https://code.claude.com/docs/en/permissions); a caixa fechada = [Sandbox](https://code.claude.com/docs/en/sandboxing); o teste antes do "pronto" = [Hooks](https://code.claude.com/docs/en/hooks); o jeito de pedir = [Boas prêÂ¡ticas](https://code.claude.com/docs/en/best-practices). Conferido em 17/11/2026.

Os 14% (pessoas que aprovam um por um) e 89% (modo automêÂ¡tico) foram mostrados na palestra; os 93% e 84% estêÂ£o nos artigos oficiais.

## Como comeêÂ§ar (sem ser têÂ©cnico)

Abra o Claude Code, ou o Codex, na pasta do seu projeto e cole:

```text
Leia o kit "IA sem estrago" em https://github.com/linnoff88-dev/ia-sem-estrago (o README explica tudo, inclusive a instalaêÂ§êÂ£o).
Depois olhe este projeto e me responda em portuguêÂªs simples:
1. O que aqui nêÂ£o teria volta se vocêÂª errasse (apagar, senhas, enviar algo para fora)?
2. Qual teste ou conferêÂªncia prova que uma tarefa ficou pronta neste projeto?
3. Quais partes do kit valem a pena para mim, e quais nêÂ£o?
NêÂ£o mude nada ainda. Mostre o plano e espere eu dizer sim.
```

A IA mostra o plano, vocêÂª aprova o que quiser e ela instala sêÂ³ isso. O kit êÂ© montado para o Claude Code; o Codex tambêÂ©m consegue ler e dizer se ele serve para o seu projeto.

## E se eu abro o Claude sem restriêÂ§êÂ£o?

Muita gente abre o Claude Code assim:

```bash
claude --chrome --dangerously-skip-permissions --exclude-dynamic-system-prompt-sections "$@"
```

**O kit continua valendo.** Testamos em 17/11/2026, no Claude Code 2.1.327, com `--dangerously-skip-permissions`:

| O que pedimos | O que aconteceu |
|---|---|
| ler o `.env` | **negado** pela trava (`Read(./.env)`) |
| `rm -rf lixo` | **negado** pela trava; a pasta ficou lêÂ¡ |
| dizer "pronto" com a checagem falhando | o hook barrou 3 vezes e depois soltou (`PRONTO_MAX`) |
| usar uma ferramenta com regra `ask` | **pediu confirmaêÂ§êÂ£o** mesmo nesse modo (no `-p`, vira recusa) |

O que muda êÂ© outra coisa: sem restriêÂ§êÂ£o, **o porteiro do modo automêÂ¡tico sai**. No modo `auto`, um segundo modelo olha cada aêÂ§êÂ£o que nêÂ£o estêÂ¡ na trava e barra o que parece estrago ou envio para fora. Com `--dangerously-skip-permissions`, tudo o que nêÂ£o estêÂ¡ na trava passa direto. Por isso:

- **Prefira `claude --permission-mode auto`** (êÂ© o padrêÂ£o desde a 2.1.283). VocêÂª tem o mesmo "nêÂ£o pede licenêÂ§a" e ainda o porteiro.
- **Se for usar sem restriêÂ§êÂ£o**, a trava do kit êÂ© a êÂºnica coisa entre a IA e o estrago: confira que ela estêÂ¡ no projeto (`python3 ferramentas/conferir.py .`). A Anthropic recomenda esse modo sêÂ³ em contêÂªiner ou mêÂ¡quina virtual.
- **`--chrome` abre o navegador**, e o navegador fica fora da caixa fechada (o sandbox sêÂ³ cerca comandos do terminal). Ponha regra `ask` nos conectores e no navegador (`kit/exemplos/conectores.json`).
- `--exclude-dynamic-system-prompt-sections` sêÂ³ mexe no texto de sistema; nêÂ£o muda nenhuma proteêÂ§êÂ£o.

---

## InstalaêÂ§êÂ£o têÂ©cnica

Para quem prefere instalar êÂ  mêÂ£o. Tudo êÂ© texto simples para copiar; nada instala sozinho.

### PrêÂ©-requisitos

- **Claude Code** com o seu projeto aberto (`claude --version`). Provado na versêÂ£o 2.1.326; `/auto-mode-setup`, `/sandbox` e `/doctor prompt-audit` foram usados nessa versêÂ£o.
- **Python 3 e git**, para o conferidor, os testes e para baixar o kit.
- **Sandbox no Linux/WSL2:** precisa de `bubblewrap` e `socat` (`sudo apt install bubblewrap socat`). No macOS nêÂ£o precisa instalar nada.

### Os arquivos

| Arquivo | Para quêÂª |
|---|---|
| `kit/.claude/settings.json` | regras de bloqueio (`.env`, `~/.ssh`, push forêÂ§ado, `rm -rf`, `reset --hard`), sandbox ligado, hooks `Stop` e `TaskCompleted` |
| `kit/.claude/hooks/pronto.sh` | roda a checagem; falhou ê¢â â saêÂ­da 2 com o motivo; no mêÂ¡ximo 3 voltas seguidas |
| `kit/teste-do-desfazer.md` | a pergunta que decide o que vai para a lista de bloqueio |
| `kit/como-e-pronto.md` | modelo de pedido com "pronto êÂ©ê¢â¬Â¦" e checagem por tarefa |
| `kit/CLAUDE.md.exemplo` | CLAUDE.md enxuto, sem IMPORTANTE em maiêÂºscula |
| `kit/exemplos/pronto-texto.json` | "pronto" para texto: hook `Stop` do tipo `agent` que confere fonte de cada afirmaêÂ§êÂ£o e nêÂºmero contra `dados.csv` |
| `kit/exemplos/conectores.json` | regras `ask` para conectores e navegador (enviar, apagar, lixeira, remover, publicar) |
| `ferramentas/conferir.py` | confere um projeto (CLAUDE.md, bloqueio + sandbox, hook do pronto); sêÂ³ lêÂª |
| `exemplo/` | um login nas trêÂªs versêÂµes (esqueceu a API velha, deslogou todo mundo, certo) + `PROVA.md` com o hook rodando de verdade |
| `guia/` | a pêÂ¡gina do guia em PT, EN e ES (GitHub Pages) |

### Como funciona

`Pedido com "pronto êÂ©ê¢â¬Â¦"` ê¢â â `Claude trabalha no auto mode` ê¢â â `bloqueio + sandbox barram o que nêÂ£o tem volta` ê¢â â `Claude tenta parar` ê¢â â `hook roda a checagem` ê¢â â `falhou: sai com 2 e volta êÂ· passou: pronto`

- **Ordem das permissêÂµes:** `deny` (bloqueia), `ask` (pergunta), `allow` (libera). O Claude Code confere `deny` primeiro, antes do verificador do auto mode, em todos os modos, inclusive `bypassPermissions`.
- **A regra olha o texto do comando**, nêÂ£o o efeito. Por isso o kit liga tambêÂ©m o **sandbox**, em que o comando sêÂ³ lêÂª as pastas e sêÂ³ fala com os sites liberados (`github.com`, `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org`). Se o seu projeto fala com outro site, acrescente o domêÂ­nio em `sandbox.network.allowedDomains`.
- **Por que `Stop` e `TaskCompleted`:** sêÂ£o os momentos em que o Claude tenta parar ou fechar uma tarefa. `PostToolUse` nêÂ£o bloqueia nem com 2, porque a ferramenta jêÂ¡ rodou.
- **SaêÂ­da 2, nêÂ£o 1:** com 2, o Claude Code devolve o erro ao Claude, que volta e conserta. Com 1, sêÂ³ mostra o erro e o Claude segue como se estivesse feito.
- **ProteêÂ§êÂ£o contra laêÂ§o:** o `pronto.sh` bloqueia no mêÂ¡ximo 3 vezes seguidas (`PRONTO_MAX`) e depois deixa parar para vocêÂª olhar.
- **Conectores e navegador** (Gmail, Drive, Slack, `--chrome`): as ferramentas se chamam `mcp__<servidor>__<aêÂ§êÂ£o>` (veja os nomes em `/mcp`). O kit sugere `ask`, nêÂ£o `deny`: `ask` continua pedindo confirmaêÂ§êÂ£o em todo modo, inclusive `--dangerously-skip-permissions`, e vocêÂª ainda consegue mandar o e-mail quando quiser. Para proibir de vez, mova a regra para `deny`. O `*` vale em qualquer parte do nome (`mcp__*__*send*`).
- **A caixa fechada sêÂ³ cerca comandos do terminal.** As ferramentas Read/Edit e os conectores ficam fora dela; por isso a trava repete `~/.ssh`, `.env` e `secrets/`. No Linux, se aparecer `Sandbox disabled: ... socat not installed`, o sandbox **nêÂ£o estêÂ¡ ligado**: instale `bubblewrap` e `socat`.
- **O modo automêÂ¡tico deixa ler o `.env` e mandar a senha para a API dela** (êÂ© o padrêÂ£o da Anthropic). Quem quer que a IA nunca veja a senha precisa da trava `Read(./.env)`, que o kit jêÂ¡ pêÂµe.
- **Diga ao modo automêÂ¡tico o que êÂ© seu.** O porteiro trata como "de fora" tudo o que nêÂ£o conhece. Liste os seus repositêÂ³rios, buckets e domêÂ­nios em `autoMode.environment`, **em `~/.claude/settings.json`** (o Claude Code ignora `autoMode` em `.claude/settings.json` do projeto, para um repositêÂ³rio nêÂ£o se autoliberar):
  ```json
  { "autoMode": { "environment": ["$defaults", "Source control: github.com/minha-org e todos os repos dela"] } }
  ```
  `$defaults` mantêÂ©m as regras da Anthropic; `/auto-mode-setup` escreve isso para vocêÂª e `claude auto-mode config` mostra o resultado.
- **Limite do prêÂ³prio Claude Code:** depois de 8 bloqueios seguidos de hook `Stop`, ele encerra sozinho (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`). O `pronto.sh` para em 3, antes disso.
- **De onde vem a checagem**, nesta ordem: a variêÂ¡vel `PRONTO_CMD`, o arquivo `.claude/pronto.cmd` (uma linha) ou a detecêÂ§êÂ£o de `npm test` / `python3 -m unittest`. Sem nada para checar, nêÂ£o bloqueia. Se juntar um `grep`, confira que a pasta existe: `! grep -rn "x" src/` passa sempre quando nêÂ£o hêÂ¡ `src/`.

## O processo, do inêÂ­cio ao fim

Troque `~/meu-projeto` pela pasta do seu projeto. ê¢Å¡â¢ê¯Â¸Â = script êÂ· ê°Å¸Â§Â  = vocêÂª (êÂ s vezes com o Claude).

| # | Passo | Comando | Quem |
|---|---|---|---|
| 0 | Baixar o kit | `git clone https://github.com/linnoff88-dev/ia-sem-estrago.git && cd ia-sem-estrago` | ê°Å¸Â§Â  vocêÂª |
| 1 | Conferir o seu projeto (falhas na 1êÂª vez sêÂ£o normais) | `python3 ferramentas/conferir.py ~/meu-projeto` | ê¢Å¡â¢ê¯Â¸Â script |
| 2 | Copiar a configuraêÂ§êÂ£o e o hook | `cp -rn kit/.claude ~/meu-projeto/` e `echo ".claude/.pronto-bloqueios" >> ~/meu-projeto/.gitignore` (o `-n` nêÂ£o sobrescreve; se jêÂ¡ houver `settings.json`, junte as chaves êÂ  mêÂ£o) | ê°Å¸Â§Â  vocêÂª |
| 3 | Dizer qual êÂ© a checagem de "pronto" (texto: junte `kit/exemplos/pronto-texto.json`) | `echo "python3 -m unittest discover -s tests -q" > ~/meu-projeto/.claude/pronto.cmd` (troque pelo teste do seu projeto) | ê°Å¸Â§Â  vocêÂª |
| 4 | Ligar o auto mode e descrever a sua casa | `claude --permission-mode auto` (ou Shift+Tab atêÂ© "ê¢ÂÂµê¢ÂÂµ auto mode on"; padrêÂ£o desde a 2.1.283), depois `/auto-mode-setup` | ê°Å¸Â§Â  vocêÂª + Claude |
| 5 | Ligar e testar o sandbox; se usa conectores ou `--chrome`, juntar `kit/exemplos/conectores.json` | `/sandbox` | ê°Å¸Â§Â  vocêÂª |
| 6 | Enxugar o CLAUDE.md | `/doctor prompt-audit` e, em cada linha, "ele descobriria isso lendo o cêÂ³digo?" | ê°Å¸Â§Â  vocêÂª + Claude |
| 7 | Ver o hook cobrar | `bash exemplo/rodar.sh` (esqueceu: 2 êÂ· deslogou: 2 êÂ· certo: 0) | ê¢Å¡â¢ê¯Â¸Â script |
| 8 | Conferir de novo | passo 1 ê¢â â `ia sem estrago: ok` | ê¢Å¡â¢ê¯Â¸Â script |

O conferidor lêÂª os arquivos; ele nêÂ£o sabe se vocêÂª rodou os passos 4 e 5 dentro do Claude Code.

## Testes

```bash
python3 -m unittest discover -s tests -v   # 12 testes, sêÂ³ Python 3
bash exemplo/rodar.sh                       # esqueceu: 2 êÂ· deslogou: 2 êÂ· certo: 0
```

## A prova

O hook rodou de verdade no Claude Code 2.1.326, pela assinatura, em 17/11/2026. Com um erro escondido (a soma subtraêÂ­a), o Claude disse "pronto"; o hook rodou o teste, viu a falha e saiu com 2; o Claude voltou, achou o erro, consertou e sêÂ³ entêÂ£o parou. Registro: `exemplo/PROVA.md`.

## De onde vem

Palestra "Rethinking Claude Code Best Practices", de Lydia Hallie (time do Claude Code, Anthropic, AI Engineer): https://www.youtube.com/watch?v=vlfCjWuv4es. Sintaxe conferida na documentaêÂ§êÂ£o oficial do Claude Code (permissions, sandboxing, hooks, auto mode) em 17/11/2026. O estudo dos 14% e 89% foi sêÂ³ mostrado na palestra. Resumo de terceiros da mesma palestra, que inspirou a trava de conectores e o "pronto" de texto: "Anthropic Engineer Explains: The New Way to Use Claude Code", de Nate Herk (PDF); conferimos cada item na documentaêÂ§êÂ£o antes de pêÂ´r no kit.

GrêÂ¡tis no [ARCKHê AI](https://ARCKHê AI), direto na internet. LicenêÂ§a MIT.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>