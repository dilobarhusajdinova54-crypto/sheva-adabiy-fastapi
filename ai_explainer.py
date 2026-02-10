def explain_word(word: str) -> str:
    explanations = {
        "ketdik": (
            "“Ketdik” — fe’lning o‘tgan zamon, ko‘plik shakli. "
            "Harakat avval bajarilganini bildiradi. "
            "Masalan: “Biz kecha soat oltida ketdik.”"
        ),
        "kelyapti": (
            "“Kelyapti” — hozirgi davom zamon fe’li. "
            "Harakat ayni paytda davom etayotganini bildiradi. "
            "Masalan: “U hozir uyga kelyapti.”"
        ),
        "ketayapti": (
            "“Ketayapti” — hozirgi davom zamon fe’li. "
            "Masalan: “Avtobus bekatdan ketayapti.”"
        )
    }

    return explanations.get(
        word,
        f"“{word}” — adabiy o‘zbek tilidagi fe’l. "
        "Bu demo versiyada AI izohlar bosqichma-bosqich boyitiladi."
    )
