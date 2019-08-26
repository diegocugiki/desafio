from src.servico.base_login_servico import BaseLoginServico
from settings import HOST_C, PORT_C

class BaseCLoginServico():
    def efetuar_login(self):
        base_login_servico = BaseLoginServico()
        return base_login_servico.efetuar_login(HOST_C, PORT_C)