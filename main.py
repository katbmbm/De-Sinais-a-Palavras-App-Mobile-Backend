from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
import json
import os
import base64
from io import BytesIO
from PIL import Image
from cont_dedos import contar_dedos

app = FastAPI()

JSON_PATH = os.path.join(os.path.dirname(__file__), "count.json")
TEMP_IMG_PATH = os.path.join(os.path.dirname(__file__), "temp_img.jpg")

@app.post("/processar")
def processar_imagem(image: str = Body(..., embed=True)):
    try:
        # Decode base64 string
        try:
            image_data = base64.b64decode(image.split(",")[-1])  # Handles optional data URI prefix
        except Exception as e:
            return JSONResponse(status_code=400, content={"error": "Invalid base64 image data"})

        # Save to temp file
        image_file = Image.open(BytesIO(image_data))
        image_file.save(TEMP_IMG_PATH)

        # Process image
        contar_dedos(TEMP_IMG_PATH)
        os.remove(TEMP_IMG_PATH)

        # Return result
        with open(JSON_PATH, "r") as f:
            data = json.load(f)
        return data

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
