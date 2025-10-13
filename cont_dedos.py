import cv2
import mediapipe as mp
import json
import sys
import os

# Arquivo de saída (com o número de dedos levantados)
JSON_PATH = os.path.join(os.path.dirname(__file__), "count.json")

def contar_dedos(img_path):
    # Carregar a imagem
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {img_path}")

    hands = mp.solutions.hands
    Hands = hands.Hands(static_image_mode=True, max_num_hands=2)
    mpDraw = mp.solutions.drawing_utils

    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape

    contador = 0

    if handPoints:
        for points in handPoints:
            pontos = []
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                pontos.append((cx, cy))

            dedos = [8, 12, 16, 20]

            if pontos:
                # Thumb (check left/right orientation)
                if pontos[5][0] < pontos[17][0]:  # thumb on left
                    if pontos[4][0] < pontos[3][0]:
                        contador += 1
                else:  # thumb on right
                    if pontos[4][0] > pontos[3][0]:
                        contador += 1

                # Other fingers
                for x in dedos:
                    if pontos[x][1] < pontos[x - 2][1]:
                        contador += 1

    # Salvar o resultado para o arquivo JSON
    with open(JSON_PATH, "w") as f:
        json.dump({"dedos levantados": contador}, f)

    print(f"Número de dedos detectados: {contador}")
    return contador

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python cont_dedos.py <caminho_da_imagem>")
        sys.exit(1)

    image_path = sys.argv[1]
    contar_dedos(image_path)
