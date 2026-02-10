"""
AI-style explanation module (DEMO)

Bu modul:
- adabiy so‘z bo‘yicha
- ta’rif
- qo‘llanish
- misollar
- Toshkent shevasidagi variantlarni
qaytaradi.

Keyinchalik bu joyga:
- OpenAI
- Wikipedia
- Lug‘at API
oson ulanadi.
"""

def explain_word(word: str):
    EXPLANATIONS = {
        "ketdik": {
            "definition": (
                "«Ketdik» — «ketmoq» feʼlining "
                "o‘tgan zamondagi, ko‘plik birinchi shaxs shakli."
            ),
            "usage": (
                "Gapiruvchi va u bilan birga bo‘lgan odamlar "
                "birgalikda joyni tark etganini bildiradi."
            ),
            "examples": [
                "Biz darsdan keyin uyga ketdik.",
                "Do‘stlar bilan birga shaharga ketdik."
            ],
            "dialects": {
                "Toshkent shevasi": ["kettu", "ketti"],
                "Og‘zaki nutq": ["ketvoldik"]
            }
        },

        "kelyapti": {
            "definition": (
                "«Kelyapti» — «kelmoq» feʼlining "
                "hozirgi zamon davomiy shakli."
            ),
            "usage": (
                "Harakat hozirgi paytda davom etayotganini bildiradi."
            ),
            "examples": [
                "U hozir ishga kelyapti.",
                "Mehmonlar biznikiga kelyapti."
            ],
            "dialects": {
                "Toshkent shevasi": ["kevotti"],
                "Og‘zaki nutq": ["kelvotti"]
            }
        }
    }

    return EXPLANATIONS.get(word)
