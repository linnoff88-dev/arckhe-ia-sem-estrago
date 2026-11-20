#!/usr/bin/env bash
# Mostra o hook pronto.sh cobrando as três versões do exemplo do login.
# Uso: bash exemplo/rodar.sh
set -u
AQUI=$(cd "$(dirname "$0")" && pwd)
HOOK="$AQUI/../kit/.claude/hooks/pronto.sh"
for v in esqueceu deslogou certo; do
  rm -f "$AQUI/login-api/.claude/.pronto-bloqueios"
  echo '{"stop_hook_active": false}' | LOGIN_VERSAO=$v CLAUDE_PROJECT_DIR="$AQUI/login-api" \
    PRONTO_CMD="python3 -m unittest discover -s tests -q" bash "$HOOK" 2>/dev/null
  rc=$?
  case $rc in
    0) echo "$v: saída 0 → pronto de verdade";;
    2) echo "$v: saída 2 → o Claude volta e conserta";;
    *) echo "$v: saída $rc";;
  esac
done
rm -f "$AQUI/login-api/.claude/.pronto-bloqueios"
