import requests
from bs4 import BeautifulSoup

URL = "https://www.tgju.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(
        URL,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("Status:", response.status_code)
    print("=" * 70)

    keywords = [
        "تتر",
        "طلای 18 عیار",
        "مثقال طلا",
        "سکه امامی",
        "نیم سکه",
        "ربع سکه",
        "انس جهانی طلا"
    ]

    for keyword in keywords:

        print(f"\n🔎 {keyword}")

        found = False

        for text in soup.find_all(string=lambda t: t and keyword in t):

            element = text.parent

            print("TEXT:", text.strip()[:100])
            print("ELEMENT:", element.name)
            print("HTML اطراف:")

            # نمایش والدهای نزدیک
            parent = element

            for level in range(4):
                if parent:
                    print(f"\n--- Level {level} ---")
                    print(str(parent)[:2000])
                    parent = parent.parent

            found = True
            break

        if not found:
            print("❌ پیدا نشد")

    print("\n" + "=" * 70)

except Exception as e:
    print("❌ ERROR:", e)
    raise
