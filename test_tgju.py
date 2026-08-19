import requests
from bs4 import BeautifulSoup
import re

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

    text = soup.get_text(" ", strip=True)

    match = re.search(
        r"نرخ فعلی\s*:?\s*([0-9۰-۹][0-9۰-۹,٫.]*)",
        text
    )

    if match:
        price = match.group(1)
        print("✅ تتر:", price)
    else:
        print("❌ قیمت تتر پیدا نشد")

except Exception as e:
    print("❌ ERROR:", e)
    raise
