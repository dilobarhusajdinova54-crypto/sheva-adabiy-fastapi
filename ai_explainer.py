import requests

def normalize(word):
    # oddiy normalization
    if word.endswith("yapti"):
        return word.replace("yapti", "moq")
    return word

def explain_word(word: str) -> str:
    base_word = normalize(word)

    try:
        url = f"https://uz.wikipedia.org/api/rest_v1/page/summary/{base_word}"
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            extract = data.get("extract")

            if extract:
                return extract

    except Exception as e:
        print("Wiki error:", e)

    return f"{word} ҳақида маълумот топилмади"
