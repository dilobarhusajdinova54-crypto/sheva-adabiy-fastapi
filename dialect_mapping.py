DIALECT_MAP = {
    "мен мактабга кетяпман": "мен мактабга бораяпман",
    "кетвотти": "кетяпти",
    "кетвоман": "кетяпман",
}

def map_dialect(text: str):
    if not text:
        return None, None

    text = text.lower().strip()

    if text in DIALECT_MAP:
        return text, DIALECT_MAP[text]

    return None, None
