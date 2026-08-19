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

    prices = soup.find_all(
        "td",
        class_="text-left"
    )

    if len(prices) > 1:

        price = prices[1].get_text(" ", strip=True)

        print("✅ تتر:", price)

    else:

        print("❌ قیمت تتر پیدا نشد")

except Exception as e:

    print("❌ ERROR:", e)
    raise
