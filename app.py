from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import re

from pymongo import MongoClient
from dialect_mapping import map_dialect
from ai_explainer import explain_word

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

# ---------------- MongoDB ----------------
MONGO_URL = os.getenv("MONGO_URL")
col = None

if MONGO_URL:
    try:
        client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=3000)
        db = client["dialect_db"]
        col = db["toshkent_mapping"]
        client.server_info()
        print("✅ MongoDB connected")
    except Exception as e:
        print("⚠️ MongoDB disabled:", e)
        col = None

# ---------------- API ----------------
@app.post("/translate_text")
async def translate_text(payload: dict = Body(...)):
    raw_text = payload.get("text", "")

    if not raw_text:
        return {"error": "text field is required"}

    text = raw_text.lower().strip()

    literary_word = None
    source = "mapping"

    # MongoDB lookup
    if col:
        try:
            doc = col.find_one({"dialect_word": text})
            if doc:
                literary_word = doc.get("literary_word")
                source = "mongodb"
        except Exception as e:
            print("Mongo error:", e)

    # Static mapping
    if not literary_word:
        result = map_dialect(text)
        if isinstance(result, tuple):
            _, literary_word = result
        else:
            literary_word = result

    # AI explanation
    ai_explanation = None
    if literary_word:
        try:
            ai_explanation = explain_word(literary_word)
        except Exception as e:
            ai_explanation = "Izoh topilmadi"
            print("AI error:", e)

    return {
        "recognized_text": text,
        "literary_word": literary_word,
        "mapped": literary_word,
        "source": source,
        "ai_explanation": ai_explanation,
        "explanation": ai_explanation
    }
