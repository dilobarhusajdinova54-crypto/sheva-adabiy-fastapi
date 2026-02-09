from fastapi import FastAPI, UploadFile, File, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import List
import shutil
import os
import re
from pymongo import MongoClient

from speech_to_text import recognize_speech
from dialect_mapping import map_dialect

# ---------------- APP ----------------
app = FastAPI()

# ---------------- STATIC ----------------
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

# ---------------- MONGODB ----------------
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client["dialect_db"]
col = db["toshkent_mapping"]

# ---------------- TEXT TRANSLATION ----------------
@app.post("/translate_text")
async def translate_text(payload: dict = Body(...)):
    # 1. Келган матн
    raw_text = payload.get("text", "")

    # 2. Нормализация
    text = raw_text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)

    # 3. MongoDB'dan қидириш
    doc = col.find_one({
        "dialect_word": text
    })

    if doc:
        return {
            "recognized_text": text,
            "literary_word": doc.get("literary_word", ""),
            "source": "mongodb"
        }

    # 4. Агар MongoDB'da йўқ бўлса → static mapping
    dialect, literary = map_dialect(text)

    return {
        "recognized_text": text,
        "literary_word": literary,
        "source": "mapping"
    }
