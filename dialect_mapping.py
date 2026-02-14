# dialect_mapping.py

DIALECT_MAP = {
    "kevotti": "kelyapti",
    "ketvotti": "ketyapti",
    "kettu": "ketdik",
    "ketvomman": "ketyapman",
    "kettim": "ketdim",
    "qivotti": "qilyapti",
    "chiiqvotti": "chiqyapti",
    "ovotti": "olyapti"
}

def map_dialect(word):
    word = word.lower().strip()

    if word in DIALECT_MAP:
        return word, DIALECT_MAP[word]

    return word, word
