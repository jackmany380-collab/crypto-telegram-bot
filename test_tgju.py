import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

# فقط برای پیدا کردن صفحه واقعی تتر
url = "https://www.tgju.org/"

try:
    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    print("Status:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    print("\n🔎 لینک‌هایی که مربوط به تتر هستند:\n")

    found = 0

    for link in soup.find_all("a", href=True):

        text = link.get_text(" ", strip=True)

        if "تتر" in text:

            print("TEXT:", text)
            print("HREF:", link["href"])
            print("-" * 50)

            found += 1

    print("\nتعداد لینک‌های پیدا شده:", found)

except Exception as e:
    print("❌ ERROR:", e)
    raise
