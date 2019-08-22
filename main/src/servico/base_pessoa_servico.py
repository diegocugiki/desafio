import requests


class BasePessoaServico():
    def obter_dados_pessoa(self, cpf: str, token: str, porta: int):
        url_pessoa = obter_url(porta)
        dados_pessoa = obter_dados(cpf, token)
        cabecalho = obter_cabecalho()
        requisicao_usuario = requests.post(url_pessoa, json=dados_pessoa, headers=cabecalho)
        return requisicao_usuario.json()


def obter_url(porta: int):
    return f'http://localhost:{porta}/obter_pessoa'


def obter_cabecalho():
    return {
        'Content-Type': 'application/json'
    }


def obter_dados(cpf: str, token: str):
    return {
        'cpf': cpf,
        'token': token
    }