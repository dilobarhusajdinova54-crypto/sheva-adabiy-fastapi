import os
import json
import wave
from datetime import datetime

from pymongo import MongoClient
from vosk import Model, KaldiRecognizer

# ===== MongoDB ulanish =====
client = MongoClient("mongodb://localhost:27017/")
db = client["dialect_db"]
collection = db["records"]

# ===== Vosk model =====
model = Model("vosk-model-small-uz-0.22")

# ===== Dialekt -> Adabiy mapping =====
DIALECT_MAP = {
    "кетту": "кетдик",
    "борду": "бордик",
    "қилду": "қилдик",
    "келду": "келдик",
    "этту": "айтдик",
    "кўрду": "кўрдик",
    "олду": "олдик",
    "билду": "билдик",
    "ёзду": "ёздик",
    "чиқту": "чиқдик"
}

AUDIO_DIR = "."

for file in os.listdir(AUDIO_DIR):
    if file.endswith(".wav") and not file.endswith("_clean.wav"):

        print(f"\nTanish boshlandi: {file}")

        wf = wave.open(file, "rb")
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)

        result_text = ""

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                result_text += res.get("text", "") + " "

        final_res = json.loads(rec.FinalResult())
        result_text += final_res.get("text", "")

        result_text = result_text.strip()

        # Dialekt so‘zini aniqlash
        dialect_word = None
        literary_word = None

        for d, l in DIALECT_MAP.items():
            if d in result_text:
                dialect_word = d
                literary_word = l
                break

        document = {
            "audio_file": file,
            "recognized_text": result_text,
            "dialect_word": dialect_word,
            "literary_word": literary_word,
            "model": "vosk-uz",
            "sample_rate": wf.getframerate(),
            "created_at": datetime.now()
        }

        collection.insert_one(document)
        print(" → MongoDB ga saqlandi")

print("\nBarcha fayllar qayta ishlandi.")
