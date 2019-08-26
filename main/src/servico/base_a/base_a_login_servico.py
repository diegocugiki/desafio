from src.servico.base_login_servico import BaseLoginServico
from settings import HOST_A, PORT_A

class BaseALoginServico():
    def efetuar_login(self):
        base_login_servico = BaseLoginServico()
        return base_login_servico.efetuar_login(HOST_A, PORT_A)