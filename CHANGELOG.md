# Changelog

## 1.2.5 — 18/11/2026
- Dois vídeos no guia (PT/EN/ES) e nos READMEs: para quem já usa o Claude Code (https://www.youtube.com/watch?v=uBUpckFw1Xg) e para quem está começando (https://www.youtube.com/watch?v=JBiVZj8z-Ms). Narração em português, com o nome antigo "fora do volante".

## 1.2.4 — 17/11/2026
- "Pronto" para texto: `kit/exemplos/pronto-texto.json`, hook `Stop` do tipo `agent` que confere fonte e número contra `dados.csv`. Provado: relatório com 100 virou 120 com link (`exemplo/PROVA.md`, prova 2).
- Conectores e navegador: `kit/exemplos/conectores.json` com regras `ask` (enviar, apagar, lixeira, remover, publicar), que pedem confirmação em todo modo.
- Trava ampliada: `Read/Edit(./secrets/**)` e `~/**/secrets` no sandbox (`.env.local` já era coberto por `.env.*`).
- README: seção "E se eu abro o Claude sem restrição?" com o teste em `--dangerously-skip-permissions` (trava, hook e `ask` seguem valendo; sai o porteiro do modo automático), `autoMode.environment` com `$defaults` em `~/.claude/settings.json`, limite de 8 bloqueios do Claude Code, aviso do sandbox sem `socat`.
- Guia (PT/EN/ES): seção "Lista clara" (trancado, pede confirmação, cobrado antes do pronto, segue sozinho, o que não faz), cenário do relatório e duas perguntas novas (modo sem restrição; navegador e conectores).
- Fonte de terceiros citada: resumo em PDF de Nate Herk da mesma palestra, cada item conferido na documentação.

## 1.1.4 — 17/11/2026
- Seção "De onde vem" no topo do guia e "Baseado na Anthropic" nos READMEs: palestra do time do Claude Code, artigos oficiais (auto mode: 93% dos pedidos aceitos; sandbox: 84% menos pedidos) e cada peça ligada à documentação oficial.

## 1.1.3 — 17/11/2026
- Novo nome: **IA sem estrago** (antes "Fora do volante"). Repositório `inematds/ia-sem-estrago`; o endereço antigo do GitHub redireciona.
- Guia reescrito para leigos: o ganho (antes e depois), como muda o dia, como funciona sem jargão, como começar pedindo à IA para analisar o kit, a prova e perguntas comuns. A parte técnica saiu do guia e foi para o README ("Instalação técnica").
- `ferramentas/conferir_volante.py` virou `ferramentas/conferir.py`; a saída final é `ia sem estrago: ok`.
- Banners novos (PT/EN/ES) com o novo nome.

## 1.0.3 — 17/11/2026
- Seção "Explicado em 1 minuto" no guia (PT/EN/ES) e "Em 1 minuto" nos 3 READMEs: problema, de onde veio, as três trocas, o kit, a prova e o que é grátis.

## 1.0.2 — 17/11/2026
- `kit/CLAUDE.md.exemplo`: título sem "NÃO" em maiúscula (o modelo seguia a própria regra só pela metade).

## 1.0.1 — 17/11/2026
- `kit/CLAUDE.md.exemplo`: a linha que pedia "sem IMPORTANTE/NUNCA" escrevia as próprias palavras em maiúscula e o conferidor acusava o modelo; agora diz "palavras de alarme em caixa alta".
- Guia publicado (landing + guia de uso em PT, EN e ES) em `guia/`, GitHub Pages por Actions; READMEs em EN e ES.
- Passo 2 com `cp -rn` (não sobrescreve um `settings.json` que já exista).

## 1.0.0 — 17/11/2026
- Kit inicial: settings (deny, sandbox, Stop/TaskCompleted), pronto.sh (saída 2, até 3 voltas), conferir_volante.py, exemplo do login, prova real no Claude Code 2.1.326, 11 testes.
