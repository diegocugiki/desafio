from src.modelo.dados_pessoa import DadosPessoa
from src.servico.base_a.base_a_login_servico import BaseALoginServico
from src.servico.base_a.base_a_pessoa_servico import BaseAPessoaServico
from src.servico.base_b.base_b_login_servico import BaseBLoginServico
from src.servico.base_b.base_b_pessoa_servico import BaseBPessoaServico
from src.servico.base_c.base_c_login_servico import BaseCLoginServico
from src.servico.base_c.base_c_pessoa_servico import BaseCPessoaServico

class CargaDadosPessoaServico():
    def obter_dados_pessoa_base_a(self, dados: DadosPessoa):
        base_a_login_servico = BaseALoginServico()
        token_base_a = base_a_login_servico.efetuar_login()
        base_a_pessoa_servico = BaseAPessoaServico()
        return base_a_pessoa_servico.obter_dados_pessoa(dados.cpf, token_base_a)

    def obter_dados_pessoa_base_b(self, dados: DadosPessoa):
        base_b_login_servico = BaseBLoginServico()
        token_base_b = base_b_login_servico.efetuar_login()
        base_b_pessoa_servico = BaseBPessoaServico()
        return base_b_pessoa_servico.obter_dados_pessoa(dados.cpf, token_base_b)

    def obter_dados_pessoa_base_c(self, dados: DadosPessoa):
        base_c_login_servico = BaseCLoginServico()
        token_base_c = base_c_login_servico.efetuar_login()
        base_c_pessoa_servico = BaseCPessoaServico()
        return base_c_pessoa_servico.obter_dados_pessoa(dados.cpf, token_base_c)
