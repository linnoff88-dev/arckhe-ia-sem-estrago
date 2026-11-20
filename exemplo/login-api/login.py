"""Exemplo do vídeo: mudar o login para a API nova.

Três versões que "parecem certas de longe" (escolha com LOGIN_VERSAO):
  esqueceu  — mudou, mas o login ainda chama a API velha
  deslogou  — mudou e derrubou as sessões abertas
  certo     — mudou tudo e manteve as sessões
"""
import os

VERSAO = os.environ.get("LOGIN_VERSAO", "certo")


class ApiVelha:
    nome = "velha"

    def autenticar(self, usuario, senha):
        return f"token-velho-{usuario}"


class ApiNova:
    nome = "nova"

    def autenticar(self, usuario, senha):
        return f"token-novo-{usuario}"

    def migrar_sessao(self, token_velho):
        return token_velho.replace("token-velho-", "token-novo-")


def api_do_login():
    return ApiVelha() if VERSAO == "esqueceu" else ApiNova()


def entrar(usuario, senha):
    return api_do_login().autenticar(usuario, senha)


def migrar_sessoes(sessoes):
    """Recebe {usuario: token} da API velha e devolve as sessões na API nova."""
    if VERSAO == "deslogou":
        return {}
    nova = ApiNova()
    return {u: nova.migrar_sessao(t) for u, t in sessoes.items()}
