from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import json
import base64
import requests
from PIL import Image
from io import BytesIO
from cont_dedos import contar_dedos  # Importar apenas a função para n pegar o módulo MediaPipe

app = FastAPI()

# Paths
BASE_DIR = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_DIR, "count.json")
TEMP_IMG_PATH = os.path.join(BASE_DIR, "temp_img.jpg")

# Model for base64 input
class Base64ImageRequest(BaseModel):
    image_base64: str

@app.get("/")
def read_root():
    return {"message": "API de Contagem de Dedos"}

@app.get("/processar")
def processar_imagem(img_path: str = Query(..., description="Caminho da imagem ou URL")):
    try:
        # Handle remote image URL
        if img_path.startswith("http://") or img_path.startswith("https://"):
            response = requests.get(img_path)
            if response.status_code != 200:
                return JSONResponse(status_code=404, content={"error": f"Could not download image: {img_path}"})
            image = Image.open(BytesIO(response.content))
            image.save(TEMP_IMG_PATH)
            contar_dedos(TEMP_IMG_PATH)
            os.remove(TEMP_IMG_PATH)

        # Handle local image path
        else:
            if not os.path.exists(img_path):
                return JSONResponse(status_code=404, content={"error": f"Image not found: {img_path}"})
            contar_dedos(img_path)

        # Return result
        with open(JSON_PATH, "r") as f:
            data = json.load(f)
        return data

    except FileNotFoundError as e:
        return JSONResponse(status_code=404, content={"error": str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/processar_base64")
def processar_base64_image(payload: Base64ImageRequest):
    try:
        # Decode base64 string
        image_data = base64.b64decode(payload.image_base64)
        image = Image.open(BytesIO(image_data))
        image.save(TEMP_IMG_PATH)

        # Process image
        contar_dedos(TEMP_IMG_PATH)
        os.remove(TEMP_IMG_PATH)

        # Return result
        with open(JSON_PATH, "r") as f:
            data = json.load(f)
        return data

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
