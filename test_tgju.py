import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://www.tgju.org/profile/crypto-tether"

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    print("Status:", response.status_code)

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    price = soup.find(
        "td",
        class_="text-left"
    )

    if price:
        value = price.get_text(strip=True)
        print("✅ تتر:", value)
    else:
        print("❌ قیمت تتر پیدا نشد")

except Exception as e:
    print("❌ ERROR:", e)
    raise
