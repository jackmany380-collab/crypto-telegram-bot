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

    print("\nتعداد td های text-left:", len(prices))
    print("\nمقادیر پیدا شده:\n")

    for i, item in enumerate(prices):
        value = item.get_text(" ", strip=True)

        if value:
            print(f"{i}: {value}")

except Exception as e:
    print("❌ ERROR:", e)
    raise
