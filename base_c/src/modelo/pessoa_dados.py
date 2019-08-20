from pydantic import BaseModel

class PessoaDados(BaseModel):
    ultima_consulta: dict
    movimentacao_financeira: dict
    ultima_compra_cartao_credito: dict
