from pydantic import BaseModel

class Pessoa(BaseModel):
    cpf: str
    token: str