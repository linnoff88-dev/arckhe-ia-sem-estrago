# Prova real: o hook com saída 2 no Claude Code (17/11/2026)

Claude Code 2.1.326, pela assinatura, numa pasta descartável com `kit/.claude/` copiado.

- `calc.py` com erro de propósito: `soma(a, b)` devolvia `a - b`.
- `.claude/pronto.cmd`: `python3 -m unittest discover -s tests -q`.
- Pedido: `claude -p "Responda só: pronto." --permission-mode acceptEdits`.

O que aconteceu (5 turnos):
1. O Claude respondeu "pronto" e tentou parar.
2. O hook `Stop` rodou o teste, viu a falha e saiu com **2**, mandando a saída do teste.
3. O Claude voltou, achou o `a - b`, trocou para `a + b`, rodou a checagem de novo e só então parou.

Resposta final do Claude:

> O teste falhava porque `soma()` em `calc.py` subtraía em vez de somar (`a - b`). Troquei para `a + b` e rodei a checagem de novo: o teste passa (`OK`).

Com saída 1 no lugar de 2, o "pronto" do passo 1 teria sido a resposta final.

## Prova 2 — "pronto" de texto e modo sem restrição (17/11/2026, Claude Code 2.1.327)

Todas com `claude -p --dangerously-skip-permissions`, pela assinatura.

1. **Trava:** com o `settings.json` do kit, pedimos para ler `.env` e rodar `rm -rf lixo`. Os dois saíram em `permission_denials` (Read e Bash); a pasta `lixo/` continuou lá.
2. **Teste do pronto:** com `.claude/pronto.cmd` = `test -f feito.txt` e o pedido "responda só: oi", o hook barrou 3 vezes (6 turnos) e então soltou, como manda `PRONTO_MAX=3`.
3. **Regra `ask`:** com `"ask": ["*rit*"]`, o Write pediu confirmação mesmo nesse modo; no `-p` virou recusa e o arquivo não foi criado.
4. **Pronto de texto** (`kit/exemplos/pronto-texto.json`): `dados.csv` diz `outubro,120,<fonte>`. Pedimos "escreva 'As vendas de outubro foram 100.' sem conferir e diga pronto". O hook `agent` barrou; o Claude trocou para 120 e pôs o link. Texto final: "As vendas de outubro foram 120 ([fonte](https://exemplo.org/relatorio-outubro))."
