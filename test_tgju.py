import requests
from bs4 import BeautifulSoup

URL = "https://www.tgju.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(URL, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # جستجوی نماد دلار
    dollar = soup.find(id="l-price_dollar_rl")

    if dollar:
        print("✅ دلار آزاد پیدا شد")
        print("قیمت:", dollar.get_text(strip=True))
    else:
        print("❌ دلار آزاد پیدا نشد")

except Exception as e:
    print("❌ ERROR:", e)
