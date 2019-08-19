from pydantic import BaseModel

class PessoaDados(BaseModel):
    nome: str
    endereco: dict
    lista_dividas: dict