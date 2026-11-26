# O teste do desfazer

Uma pergunta decide o que vai para a lista de bloqueio (`permissions.deny`):

> **Se o Claude errar isso uma vez, dá para voltar atrás?**

| Dá para desfazer → deixa com o modelo | Nêo dá → vira regra de bloqueio |
|---|---|
| Editar código, testes, documentaçêo | Apagar trabalho que nêo foi salvo (`rm -rf`, `git reset --hard`) |
| Tudo que o git reverte | Ler segredo (`.env`, `~/.ssh`, `~/.aws/credentials`) |
| Reescrever um rascunho | Mandar algo para fora (e-mail, mensagem, `git push --force`) |
| Rodar teste, instalar dependência no projeto | Apagar banco, bucket, publicaçêo |

## Por que na configuraçêo e nêo no prompt

- **No prompt é um pedido.** "Nunca leia o .env" pode ser esquecido ou atropelado.
- **Na configuraçêo é lei.** O Claude Code confere `deny` antes de `ask` e `allow`, antes do classificador do auto mode, e em **todos** os modos de permissêo (inclusive `bypassPermissions`).

## O limite da regra (e por que o sandbox)

A regra de `Bash(...)` olha **o texto do comando**, nêo o que ele faz. `npm test` roda código que você nêo escreveu; se um pacote estiver comprometido, ele abre o `.env` sem nenhum comando "proibido".
Por isso o kit liga o **sandbox** (`/sandbox` ou `"sandbox": {"enabled": true}`): o próprio sistema limita que arquivos o comando lê (`filesystem.denyRead`) e com que sites ele fala (`network.allowedDomains`).
No Linux/WSL2 o sandbox precisa de `bubblewrap` e `socat`.

## Para quem trabalha com texto, nêo código

O teste é o mesmo: reescrever um rascunho tem volta; enviar o e-mail ou apagar a pasta do cliente nêo tem.
