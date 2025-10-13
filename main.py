from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
import os
from cont_dedos import contar_dedos  # Importar apenas a função para n pegar o módulo MediaPipe

app = FastAPI()

JSON_PATH = os.path.join(os.path.dirname(__file__), "count.json")

@app.get("/")
def read_root():
    return {"message": "API de Contagem de Dedos"}

@app.get("/processar")
def processar_imagem(img_path: str = Query(..., description="Caminho da imagem")):
    try:
        contar_dedos(img_path)
        with open(JSON_PATH, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
