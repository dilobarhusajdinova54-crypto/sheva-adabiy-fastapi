from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import re

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from dialect_mapping import map_dialect

# ---------------- APP ----------------
app = FastAPI()

# ---------------- STATIC ----------------
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

# ---------------- MONGODB (SAFE MODE) ----------------
MONGO_URL = os.getenv("MONGO_URL")
col = None  # default: Mongo ishlamasin

if MONGO_URL:
    try:
        client = MongoClient(
            MONGO_URL,
            serverSelectionTimeoutMS=3000
        )
        db = client["dialect_db"]
        col = db["toshkent_mapping"]
        client.server_info()  # connection test
        print("✅ MongoDB connected")
    except ServerSelectionTimeoutError:
        print("⚠️ MongoDB not reachable, fallback to static mapping")
        col = None
    except Exception as e:
        print("⚠️ MongoDB error:", e)
        col = None

# ---------------- TEXT TRANSLATION ----------------
@app.post("/translate_text")
async def translate_text(payload: dict = Body(...)):
    raw_text = payload.get("text", "")

    if not raw_text:
        return {
            "error": "text field is required"
        }

    # normalization
    text = raw_text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)

    # try MongoDB first
    if col is not None:
        try:
            doc = col.find_one({"dialect_word": text})
            if doc:
                return {
                    "recognized_text": text,
                    "literary_word": doc.get("literary_word", ""),
                    "source": "mongodb"
                }
        except Exception as e:
            # Mongo ishlamasa ham API yiqilmaydi
            print("Mongo query error:", e)

    # fallback static mapping
    _, literary = map_dialect(text)

    return {
        "recognized_text": text,
        "literary_word": literary,
        "source": "mapping"
    }
