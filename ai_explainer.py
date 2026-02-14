import requests

def explain_word(word: str) -> str:
    explanations = {
        "ketdik": (
            "“Ketdik” — ўтган замон, кўплик шаклидаги феъл. "
            "Ҳаракат аввал бажарилганини билдиради. "
            "Масалан: “Биз кеча соат олтида кетдик.”"
        ),
        "kelyapti": (
            "“Kelyapti” — ҳозирги давом замон феъли. "
            "Ҳаракат айни пайтда давом этаётганини билдиради. "
            "Масалан: “У ҳозир уйга келяпти.”"
        ),
        "ketayapti": (
            "“Ketayapti” — ҳозирги давом замон феъли. "
            "Ҳаракат ҳозир бажарилаётганини билдиради. "
            "Масалан: “Автобус бекатдан кетаяпти.”"
        )
    }

    # 1️⃣ Агар базада бўлса → шуни қайтар
    if word in explanations:
        return explanations[word]

    # 2️⃣ Wikipedia дан олиш
    try:
        url = f"https://uz.wikipedia.org/api/rest_v1/page/summary/{word}"
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            extract = data.get("extract")

            if extract:
                return extract

    except Exception as e:
        print("Wikipedia error:", e)

    # 3️⃣ fallback
    return f"“{word}” ҳақида изоҳ топилмади."
