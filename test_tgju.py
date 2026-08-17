import requests
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_price(slug):
    url = f"https://www.tgju.org/profile/{slug}"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    html = response.text

    patterns = [
        r'data-price=["\']([\d,]+)',
        r'itemprop=["\']price["\'][^>]*>\s*([\d,]+)',
        r'نرخ فعلی::\s*([\d,]+)'
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            html,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

    return None


# =========================
# قیمت‌هایی که می‌خواهیم تست کنیم
# =========================

slugs = {
    "دلار آزاد": "price_dollar_rl",
    "تتر": "crypto-tether",
    "طلای 18 عیار": "geram18",
    "مثقال طلا": "mesghal",
    "سکه امامی": "sekee",
    "نیم سکه": "nim",
    "ربع سکه": "rob",
    "انس جهانی طلا": "ons"
}


results = {}


# =========================
# دریافت قیمت‌ها
# =========================

for name, slug in slugs.items():

    try:

        price = get_price(slug)

        results[name] = price

    except Exception as e:

        results[name] = f"ERROR: {e}"


# =========================
# نمایش نتیجه
# =========================

print("")
print("========== TGJU TEST ==========")
print("")

for name, price in results.items():

    print(f"{name}: {price}")

print("")
print("================================")
