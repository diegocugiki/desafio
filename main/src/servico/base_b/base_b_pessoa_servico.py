from src.servico.base_pessoa_servico import BasePessoaServico
from settings import HOST_B, PORT_B

class BaseBPessoaServico():
    def obter_dados_pessoa(self, cpf: str, token: str):
        base_pessoa_servico = BasePessoaServico()
        return base_pessoa_servico.obter_dados_pessoa(cpf, token, HOST_B, PORT_B)