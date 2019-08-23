import uvicorn

from fastapi import FastAPI
from src.modelo.login import Login
from src.modelo.pessoa import Pessoa
from src.modelo.pessoa_dados import PessoaDados
from src.servico.login_servico import LoginServico
from src.servico.pessoa_servico import PessoaServico

app = FastAPI()

@app.post('/login')
def login(login: Login):
    return LoginServico.efetuar_login(login)

@app.post('/obter_pessoa', response_model=PessoaDados)
def obter_pessoa_dados(pessoa: Pessoa):
    return PessoaServico.obter_pessoa(pessoa)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='localhost',
        port=8001,
        debug=True,
        log_level='info',
        access_log=True,
        workers=1,
        timeout_keep_alive=50
    )