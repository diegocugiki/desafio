
from src.servico.base_pessoa_servico import BasePessoaServico

class BaseAPessoaServico():
    def obter_dados_pessoa(self, cpf: str, token: str):
        base_pessoa_servico = BasePessoaServico()
        return base_pessoa_servico.obter_dados_pessoa(cpf, token, 8000)