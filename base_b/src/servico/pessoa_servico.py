import json

from src.modelo.pessoa import Pessoa
from src.util.validacao_token import ValidacaoToken

class PessoaServico:

    def obter_pessoa(pessoa: Pessoa):
        ValidacaoToken.valida_token(pessoa.token)

        with open("../mock_base_b.json", "r") as base:
            list = json.load(base)
            return list[pessoa.cpf]

        return "Pessoa não localizada!"