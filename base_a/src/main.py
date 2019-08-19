import uvicorn

from fastapi import FastAPI
from base_a.src.modelo.login import Login
from base_a.src.modelo.pessoa import Pessoa
from base_a.src.modelo.pessoa_dados import PessoaDados
from base_a.src.servico.login_servico import efetuar_login
from base_a.src.servico.pessoa_servico import obter_pessoa

app = FastAPI()

@app.post('/login')
def login(login: Login):
    return efetuar_login(login)

@app.post('/obter_pessoa', response_model=PessoaDados)
def obter_pessoa_dados(pessoa: Pessoa):
    return obter_pessoa(pessoa)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000,
        debug=True,
        log_level="info",
        access_log=True,
        workers=1,
        timeout_keep_alive=50
    )