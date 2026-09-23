from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PlacasJogo(BaseModel):
    jogador: str
    pontos: int

@app.post("/salvar-placar")
def salvar_placar(dados: PlacasJogo):

    return {
        "status": "Placar salvo com sucesso!",
        "jogador_recebido": dados.jogador,
        "pontos_recebidos": dados.pontos
    }

