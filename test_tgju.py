import requests
from bs4 import BeautifulSoup

url = "https://www.tgju.org/profile/price_dollar_rl"

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
