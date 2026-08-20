import requests
from bs4 import BeautifulSoup

url = "https://www.tgju.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers,
    timeout=20
)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print("\n🔎 لینک‌ها و متن‌های مربوط به دلار:\n")

count = 0

for a in soup.find_all("a", href=True):

    text = a.get_text(" ", strip=True)
    href = a.get("href")

    if "دلار" in text:

        print(f"TEXT: {text}")
        print(f"HREF: {href}")
        print("-" * 60)

        count += 1

print("\nتعداد موارد:", count)
