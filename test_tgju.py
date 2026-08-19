import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0"
}

pages = {
    "تتر": "https://www.tgju.org/profile/usdt",
    "طلای 18 عیار": "https://www.tgju.org/profile/geram18",
    "مثقال طلا": "https://www.tgju.org/profile/mesghal",
    "سکه امامی": "https://www.tgju.org/profile/sekee",
    "نیم سکه": "https://www.tgju.org/profile/nim",
    "ربع سکه": "https://www.tgju.org/profile/rob",
}

for name, url in pages.items():

    print("\n" + "=" * 50)
    print(f"🔎 {name}")
    print("=" * 50)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        print("Status:", response.status_code)

        soup = BeautifulSoup(response.text, "html.parser")

        # پیدا کردن عبارت «نرخ فعلی»
        text = soup.get_text(" ", strip=True)

        match = re.search(
            r"نرخ فعلی\s*:?\s*([\d,]+(?:\.\d+)?)",
            text
        )

        if match:
            price = match.group(1)
            print(f"✅ {name}: {price}")
        else:
            print(f"❌ قیمت {name} پیدا نشد")

    except Exception as e:
        print(f"❌ ERROR: {e}")
