from pydantic import BaseModel

class PessoaDados(BaseModel):
    idade: str
    lista_bens: dict
    endereco: dict
    fonte_renda : dict