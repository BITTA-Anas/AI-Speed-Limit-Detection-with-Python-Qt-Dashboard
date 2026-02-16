import cv2
import pandas as pd
from ultralytics import YOLO
import numpy as np
import pytesseract
from datetime import datetime
import json
import threading
import queue
import torch

# =============================
# Configuration Tesseract
# =============================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# =============================
# Chargement modèle YOLO
# =============================
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"🔧 Utilisation de : {device.upper()}")
model = YOLO("Model.pt")
model.to(device)

# =============================
# Chargement des classes
# =============================
with open("SpeedClass.txt", "r") as my_file:
    class_list = my_file.read().split("\n")

# =============================
# Initialisation
# =============================
processed_numbers = set()
list1 = []
vitesses_valides = {20, 30, 40, 50, 60, 80, 100, 120}

# =============================
# Fonction OCR (inchangée)
# =============================
def lire_vitesse(crop, frame, x1, y1, x2, y2):
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 10, 20, 20)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(
        binary, config="--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789"
    ).strip()
    text = text.replace("(", "").replace(")", "").replace(",", "")

    if text and text not in processed_numbers:
        processed_numbers.add(text)
        list1.append(text)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            vitesse_num = int(text)
            if vitesse_num in vitesses_valides:
                data = {
                    "vitesse_limite": vitesse_num,
                    "timestamp": current_datetime
                }

                with open("vitesse_limite.json", "w") as json_file:
                    json.dump(data, json_file)

                with open("speed_limit_data.txt", "a") as file:
                    file.write(f"{text}\t{current_datetime}\n")

                print(f"✅ Vitesse limite détectée : {vitesse_num} km/h")
            else:
                print(f"⛔ Vitesse détectée non valide : {vitesse_num} km/h → ignorée")
        except ValueError:
            print(f"⚠️ OCR incorrect : {text}")

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
    cv2.imshow("crop", crop)

# =============================
# Thread de capture vidéo
# =============================
frame_queue = queue.Queue(maxsize=1)

def capture_frames():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (1020, 500))
        if not frame_queue.full():
            frame_queue.put(frame)
    cap.release()

threading.Thread(target=capture_frames, daemon=True).start()

# =============================
# Boucle principale de traitement
# =============================
while True:
    if frame_queue.empty():
        continue

    frame = frame_queue.get()
    results = model.predict(source=frame, stream=True, device=device)
    
    for result in results:
        boxes = result.boxes.data
        if boxes is None or len(boxes) == 0:
            continue

        px = pd.DataFrame(boxes.cpu()).astype("float")

        for _, row in px.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            c = class_list[d]

            crop = frame[y1:y2, x1:x2]
            threading.Thread(target=lire_vitesse, args=(crop, frame, x1, y1, x2, y2)).start()

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
