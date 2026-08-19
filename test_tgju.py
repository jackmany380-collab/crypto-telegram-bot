import requests
from bs4 import BeautifulSoup

URL = "https://www.tgju.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

items = {
    "دلار آزاد": "l-price_dollar_rl",
    "تتر": "l-price_usdt",
    "طلای 18 عیار": "l-price_gold_18",
    "مثقال طلا": "l-price_gold_mithqal",
    "سکه امامی": "l-price_sekee",
    "نیم سکه": "l-price_nim",
    "ربع سکه": "l-price_rob",
    "انس جهانی طلا": "l-price_xau"
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
    print("=" * 40)

    soup = BeautifulSoup(response.text, "html.parser")

    for name, item_id in items.items():

        item = soup.find(id=item_id)

        if item:
            value = item.get_text(strip=True)
            print(f"✅ {name}: {value}")
        else:
            print(f"❌ {name}: پیدا نشد")

    print("=" * 40)

except Exception as e:
    print("❌ ERROR:", e)
    raise
