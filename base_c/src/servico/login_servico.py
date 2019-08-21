from src.modelo.login import Login
from src.util.validacao_token import ValidacaoToken

class LoginServico:

    def efetuar_login(login: Login):
        if login.usuario == "mestre" and login.senha == "mestra":
            return ValidacaoToken.obtem_toke_assinado(login.usuario)

        return "Login inválido!"