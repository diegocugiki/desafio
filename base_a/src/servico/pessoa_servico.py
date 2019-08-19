import json

from base_a.src.modelo.pessoa import Pessoa
from base_a.src.util.validacao_token import valida_token

def obter_pessoa(pessoa: Pessoa):
    valida_token(pessoa.token)

    with open("mock_base_a.json", "r") as base:
        list = json.load(base)
        return list[pessoa.cpf]

    return "pessoa nao encontrada"