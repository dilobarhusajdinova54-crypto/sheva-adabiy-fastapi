DIALECT_MAP = [
    ("ketvotti", "ketayapti"),
    ("kevotti", "kelyapti"),   # ✅ ТЎҒРИ ВАРИАНТ
    ("ketvomman", "ketayapman"),
    ("kema otdi", "keldik"),
    ("borib otdi", "bordik"),
    ("chiqib otdi", "chiqdik"),
    ("obod", "bo‘ldi"),
    ("ketti", "ketdik"),
    ("kettu", "ketdik"),
]

def map_dialect(text: str):
    if not text:
        return None, None

    text = text.lower().strip()

    if text in DIALECT_MAP:
        return text, DIALECT_MAP[text]

    return None, None
