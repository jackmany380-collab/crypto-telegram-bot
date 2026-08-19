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

    # پیدا کردن تمام تگ‌هایی که احتمال دارد قیمت داخل آنها باشد
    candidates = soup.find_all(
        ["span", "div", "td", "strong"]
    )

    print("\n🔎 اعداد اطراف قیمت تتر:\n")

    count = 0

    for element in candidates:

        text = element.get_text(" ", strip=True)

        # فقط متن‌هایی که شبیه قیمت هستند
        if (
            "," in text
            and any(char.isdigit() for char in text)
            and len(text) < 100
        ):

            print(
                "TAG:",
                element.name,
                "| CLASS:",
                element.get("class"),
                "| ID:",
                element.get("id"),
                "| TEXT:",
                text
            )

            count += 1

            if count >= 30:
                break

    print("\nتعداد موارد نمایش داده شده:", count)

except Exception as e:
    print("❌ ERROR:", e)
    raise
