import uvicorn

from fastapi import FastAPI
from src.modelo.dados_pessoa import DadosPessoa
from src.servico.carga_dados_pessoa_servico import CargaDadosPessoaServico

app = FastAPI()

@app.post('/obter_dados_pessoa')
def obter_dados_pessoa(dados: DadosPessoa):

    cargaDadosPessoaServico = CargaDadosPessoaServico()

    dados_pessoa_base_a = cargaDadosPessoaServico.obter_dados_pessoa_base_a(dados)
    dados_pessoa_base_b = cargaDadosPessoaServico.obter_dados_pessoa_base_b(dados)
    dados_pessoa_base_c = cargaDadosPessoaServico.obter_dados_pessoa_base_c(dados)

    abc =  {
        'dados pessoais:': dados_pessoa_base_a,
        'score de credito:': dados_pessoa_base_b,
        'movimentacoes:': dados_pessoa_base_c,
    }
    return abc


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='localhost',
        port=9099,
        debug=True,
        log_level='info',
        access_log=True,
        workers=1,
        timeout_keep_alive=50
    )