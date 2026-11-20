#!/usr/bin/env bash
# pronto.sh — hook de Stop/TaskCompleted do kit "IA sem estrago".
# Roda a checagem de "pronto" do projeto. Falhou → sai com 2 (o Claude volta e conserta).
# Saída 1 NÃO serve: o Claude Code trata como erro que não bloqueia e segue como se estivesse feito.
#
# A checagem vem, nesta ordem, de:
#   1. variável PRONTO_CMD
#   2. arquivo .claude/pronto.cmd (uma linha, o comando)
#   3. detecção: pytest / python -m unittest / npm test
# Proteção contra laço: no máximo PRONTO_MAX bloqueios seguidos (padrão 3); depois avisa e deixa parar.
set -uo pipefail

DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$DIR" || exit 0
ENTRADA=$(cat 2>/dev/null || true)   # JSON do Claude Code (stop_hook_active etc.); lido para não travar o pipe
CONTA="$DIR/.claude/.pronto-bloqueios"
MAX="${PRONTO_MAX:-3}"

cmd="${PRONTO_CMD:-}"
[ -z "$cmd" ] && [ -s "$DIR/.claude/pronto.cmd" ] && cmd=$(head -1 "$DIR/.claude/pronto.cmd")
if [ -z "$cmd" ]; then
  if [ -f package.json ] && grep -q '"test"' package.json; then cmd="npm test --silent"
  elif [ -d tests ] || ls test_*.py >/dev/null 2>&1; then cmd="python3 -m unittest discover -s tests -q"
  fi
fi
[ -z "$cmd" ] && { rm -f "$CONTA"; exit 0; }   # nada para checar: não bloqueia

saida=$(bash -c "$cmd" 2>&1); rc=$?
if [ $rc -eq 0 ]; then rm -f "$CONTA"; exit 0; fi

n=$(( $(cat "$CONTA" 2>/dev/null || echo 0) + 1 ))
if [ "$n" -gt "$MAX" ]; then
  rm -f "$CONTA"
  echo "pronto.sh: a checagem ainda falha depois de $MAX voltas; deixo parar para você olhar. Comando: $cmd" >&2
  exit 1
fi
echo "$n" > "$CONTA"
{
  echo "Ainda não está pronto: a checagem falhou (volta $n de $MAX)."
  echo "Comando: $cmd"
  echo "Últimas linhas:"
  echo "$saida" | tail -25
  echo "Conserte e rode a checagem de novo antes de dizer pronto."
} >&2
exit 2
