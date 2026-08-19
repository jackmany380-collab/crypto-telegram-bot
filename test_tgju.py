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

    # پیدا کردن متن «نرخ فعلی»
    text = soup.get_text(" ", strip=True)

    index = text.find("نرخ فعلی")

    if index != -1:
        print("\n✅ «نرخ فعلی» پیدا شد\n")

        # نمایش 300 کاراکتر بعد از «نرخ فعلی»
        print(text[index:index + 300])

    else:
        print("❌ عبارت «نرخ فعلی» پیدا نشد")

except Exception as e:
    print("❌ ERROR:", e)
    raise
