from base_a.src.modelo.login import Login
from base_a.src.util.validacao_token import obtem_toke_assinado


def efetuar_login(login: Login):
    if login.usuario == "mestre" and login.senha == "mestra":
        return obtem_toke_assinado(login.usuario)

    return "Login inválido!"