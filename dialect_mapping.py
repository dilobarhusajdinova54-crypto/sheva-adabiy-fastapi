DIALECT_MAP = [
    ("ketvotti", "ketayapti"),
    ("kevotti", "kelyapti"),   # ✅ тўғри
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

    for dialect, literary in DIALECT_MAP:
        if dialect == text:
            return dialect, literary

    return None, None
