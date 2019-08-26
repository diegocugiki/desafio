import requests

class BaseLoginServico():
    def efetuar_login(self, host: str, porta: int):
        url_login = obter_url_login(host, porta)
        headers = obter_cabecalho()
        dados_login = obter_dados_login()
        requisicao_login = requests.post(url_login, json=dados_login, headers=headers)
        return requisicao_login.json()


def obter_url_login(host: str,porta: int):
    return f'http://{host}:{porta}/login'

def obter_cabecalho():
    return {
        'Content-Type': 'application/json'
    }

def obter_dados_login():
    return {
        'usuario': 'mestre',
        'senha': 'mestra'
    }