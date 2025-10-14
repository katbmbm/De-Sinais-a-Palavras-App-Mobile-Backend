from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
import os
import requests
from io import BytesIO
from PIL import Image
from cont_dedos import contar_dedos  # Importar apenas a função para n pegar o módulo MediaPipe

app = FastAPI()

JSON_PATH = os.path.join(os.path.dirname(__file__), "count.json")
TEMP_IMG_PATH = os.path.join(os.path.dirname(__file__), "temp_img.jpg")

@app.get("/")
def read_root():
    return {"message": "API de Contagem de Dedos"}

@app.get("/processar")
def processar_imagem(img_path: str = Query(..., description="Caminho da imagem ou URL")):
    try:
        # Check if img_path is a URL
        if img_path.startswith("http://") or img_path.startswith("https://"):
            response = requests.get(img_path)
            if response.status_code != 200:
                return JSONResponse(status_code=404, content={"error": f"Could not download image: {img_path}"})
            image = Image.open(BytesIO(response.content))
            image.save(TEMP_IMG_PATH)
            contar_dedos(TEMP_IMG_PATH)
            os.remove(TEMP_IMG_PATH)
        else:
            if not os.path.exists(img_path):
                return JSONResponse(status_code=404, content={"error": f"Image not found: {img_path}"})
            contar_dedos(img_path)

        with open(JSON_PATH, "r") as f:
            data = json.load(f)
        return data

    except FileNotFoundError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


