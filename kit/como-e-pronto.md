# Como é pronto (cole no pedido de toda tarefa grande)

O mesmo pedido pode chegar a lugares bem diferentes. Exemplo: "mude o login para a API nova".
- mudou, mas deixou a API velha lá dentro;
- mudou só para logins novos;
- mudou e deslogou todo mundo.

De longe, as três parecem certas. Por isso o pedido diz **como é pronto**, e cada parte tem a sua checagem:

```text
Tarefa: <o que fazer>

Pronto é:
- <condição que dá para checar, ex.: "os testes de login passam">
- <condição do que NÃO pode acontecer, ex.: "nenhuma sessão aberta é derrubada">
- <o que some, ex.: "nenhuma chamada à API velha no código (grep vazio)">

Divida em tarefas pequenas; cada uma com o seu teste.
No fim, me mostre a saída real de cada checagem, não um resumo (eu não estava lá para ver).
```

## Fora do código

- Relatório: toda afirmação tem link de fonte; todo número bate com a planilha.
- Post/roteiro: cabe no limite de caracteres; o título sai da frase principal.

Para texto não há `npm test`, então quem confere é outra IA. `exemplos/pronto-texto.json` traz um hook `Stop` do tipo `agent`:
antes de encerrar, ele lê o texto e a planilha (`dados.csv`) e só deixa parar se toda afirmação tiver fonte e todo número bater.
Se faltar algo, devolve `{"ok": false, "reason": "..."}` e o Claude volta para corrigir. Junte o bloco `hooks.Stop` ao seu `.claude/settings.json` e troque `dados.csv` pela sua planilha.

## O hook cobra sozinho

`.claude/hooks/pronto.sh` roda a checagem quando o Claude tenta parar (`Stop`) ou fechar uma tarefa (`TaskCompleted`).
Falhou → **sai com 2** → o Claude volta e conserta. Grave o comando em `.claude/pronto.cmd`, por exemplo:

```text
python3 -m unittest discover -s tests -q && ! grep -rn "api_velha" src/
```

> Saída 1 não bloqueia: o Claude Code mostra o erro e segue. Saída 2 é a que manda voltar.
> `PostToolUse` não bloqueia nem com 2 (a ferramenta já rodou); para cobrar "pronto", use `Stop` e `TaskCompleted`.
