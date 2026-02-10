from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import re

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from dialect_mapping import map_dialect
from ai_explainer import explain_word   # 👈 МАНА ШУ ЖОЙ МУҲИМ

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

# ---------------- MongoDB (optional) ----------------
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

    text = re.sub(r"[^\w\s]", "", raw_text.lower().strip())

    literary_word = None
    source = "mapping"

    if col:
        try:
            doc = col.find_one({"dialect_word": text})
            if doc:
                literary_word = doc.get("literary_word")
                source = "mongodb"
        except:
            pass

    if not literary_word:
        _, literary_word = map_dialect(text)

    ai_explanation = None
    if literary_word:
        ai_explanation = explain_word(literary_word)

    return {
        "recognized_text": text,
        "literary_word": literary_word,
        "source": source,
        "ai_explanation": ai_explanation
    }
