from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["dialect_db"]
collection = db["records"]

DIALECT_PHRASES = {
    "ketvotti": "ketdik",
    "ketdi": "ketdik",
    "chiqib otdi": "chiqdik",
    "borib otdi": "bordik",
    "kema otdi": "keldik",
    "obod": "bo‘ldi"
}

updated = 0

for doc in collection.find({"literary_word": None}):
    text = doc.get("recognized_text", "").lower()

    for phrase, literary in DIALECT_PHRASES.items():
        if phrase in text:
            collection.update_one(
                {"_id": doc["_id"]},
                {"$set": {
                    "dialect_word": phrase,
                    "literary_word": literary
                }}
            )
            updated += 1
            break

print(f"Phrase-based mapping tugadi. Yangilandi: {updated}")
