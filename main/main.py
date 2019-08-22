import requests
import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.post('/base_a_efetua_login')
def base_a_efeua_login():
    url = "http://localhost:8000/login"
    headers = {
        'Content-Type': 'application/json'
    }
    dados = {
        'usuario': 'mestre',
        'senha': 'mestra'
    }
    requisicao = requests.get(url, headers=headers, json=dados)
    return requisicao.json()

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='localhost',
        port=8003,
        debug=True,
        log_level='info',
        access_log=True,
        workers=1,
        timeout_keep_alive=50
    )