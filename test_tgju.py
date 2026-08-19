import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://www.tgju.org/"

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    print("Status:", response.status_code)

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # پیدا کردن لینک انس جهانی طلا
    links = soup.find_all("a", href=True)

    print("\n🔎 لینک‌های مربوط به انس طلا:\n")

    for link in links:

        text = link.get_text(" ", strip=True)

        if "انس طلا" in text:

            print("TEXT:", text)
            print("HREF:", link["href"])
            print("-" * 50)

except Exception as e:
    print("❌ ERROR:", e)
    raise
