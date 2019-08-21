import jwt

from fastapi import HTTPException
from time import time

segredo = "987-654-321"

class ValidacaoToken:

    def valida_token(token: str):
        try:
            jwt.decode(token, segredo, algorithm='HS256')
        except:
            raise HTTPException(status_code=401, detail="Seu token esta inválido!")

    def obtem_toke_assinado(usuario: str):
        payload = {
            "uid": usuario,
            "exp": int(time()) + 360
        }
        return jwt.encode(payload, segredo, algorithm='HS256')