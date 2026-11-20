"""Como é pronto, em teste: o login usa a API nova E ninguém é deslogado."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import login  # noqa: E402


class ComoEPronto(unittest.TestCase):
    def test_login_usa_api_nova(self):
        self.assertTrue(login.entrar("ana", "x").startswith("token-novo-"))

    def test_ninguem_e_deslogado(self):
        abertas = {"ana": "token-velho-ana", "bia": "token-velho-bia"}
        self.assertEqual(set(login.migrar_sessoes(abertas)), {"ana", "bia"})


if __name__ == "__main__":
    unittest.main()
