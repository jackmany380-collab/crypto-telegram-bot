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

    print("Status:", response.status_code)
    print("Length:", len(response.text))
    print("=" * 60)

    soup = BeautifulSoup(response.text, "html.parser")

    # کلمات مورد نظر
    keywords = [
        "تتر",
        "طلای 18",
        "طلای ۱۸",
        "مثقال طلا",
        "سکه",
        "نیم سکه",
        "ربع سکه",
        "انس طلا"
    ]

    # پیدا کردن عناصری که این کلمات را در متن دارند
    for keyword in keywords:
        print(f"\n🔎 جستجوی: {keyword}")

        found = False

        for element in soup.find_all(string=lambda text: text and keyword in text):

            parent = element.parent

            print("TEXT:", element.strip())
            print("TAG:", parent.name)
            print("ID:", parent.get("id"))
            print("CLASS:", parent.get("class"))

            found = True

            # فقط چند نتیجه اول
            break

        if not found:
            print("❌ پیدا نشد")

    print("\n" + "=" * 60)

except Exception as e:
    print("❌ ERROR:", e)
    raise
