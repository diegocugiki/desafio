from unittest import TestCase
#from unittest.mock import patch

from src.modelo.login import Login
from src.servico.login_servico import LoginServico


class TestLoginServico(TestCase):

    #@patch('util.ValidacaoToken.obtem_toke_assinado', return_value="token_abc")
    def test_efetuar_login_informando_usuario_e_senha_corretos(self):
        login = Login(usuario="mestre", senha="mestra")
        retorno = LoginServico().efetuar_login()
        self.assertNotEqual(retorno, "Login inválido!")
