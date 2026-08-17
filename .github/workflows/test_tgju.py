import requests
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_page(url):
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    return response.text


def extract_price(html):

    patterns = [
        r'"price"\s*:\s*"?(.*?)"?[,}]',
        r'"current_price"\s*:\s*"?(.*?)"?[,}]',
        r'data-price=["\'](.*?)["\']'
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            html,
            re.IGNORECASE
        )

        if match:
            value = match.group(1)

            value = re.sub(
                r"[^\d.]",
                "",
                value
            )

            if value:
                return value

    return None


# ==========================================
# TEST URLS
# ==========================================

urls = {

    "دلار آزاد":
        "https://www.tgju.org/profile/price_dollar_rl",

    "تتر":
        "https://www.tgju.org/profile/crypto-tether",

    "طلای 18 عیار":
        "https://www.tgju.org/profile/geram18",

    "مثقال طلا":
        "https://www.tgju.org/profile/mesghal",

    "سکه امامی":
        "https://www.tgju.org/profile/sekee",

    "نیم سکه":
        "https://www.tgju.org/profile/nim",

    "ربع سکه":
        "https://www.tgju.org/profile/rob",

    "انس جهانی طلا":
        "https://www.tgju.org/profile/ons"
}


print("")
print("========== MARKET TEST ==========")
print("")


for name, url in urls.items():

    try:

        html = get_page(url)

        price = extract_price(html)

        print(f"{name}: {price}")

    except Exception as e:

        print(f"{name}: ERROR - {e}")


print("")
print("==================================")
