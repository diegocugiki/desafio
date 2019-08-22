import requests

class BaseLoginServico():
    def efetuar_login(self, porta: int):
        url_login = obter_url_login(porta)
        headers = obter_cabecalho()
        dados_login = obter_dados_login()
        requisicao_login = requests.post(url_login, json=dados_login, headers=headers)
        return requisicao_login.json()


def obter_url_login(porta: int):
    return f'http://localhost:{porta}/login'

def obter_cabecalho():
    return {
        'Content-Type': 'application/json'
    }

def obter_dados_login():
    return {
        'usuario': 'mestre',
        'senha': 'mestra'
    }