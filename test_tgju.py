import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

# صفحات TGJU
pages = {
    "تتر": "https://www.tgju.org/profile/crypto-tether",
    "طلای 18 عیار": "https://www.tgju.org/profile/geram18",
    "مثقال طلا": "https://www.tgju.org/profile/mesghal",
    "سکه امامی": "https://www.tgju.org/profile/sekee",
    "نیم سکه": "https://www.tgju.org/profile/nim",
    "ربع سکه": "https://www.tgju.org/profile/rob",
    "انس جهانی طلا": "https://www.tgju.org/profile/ons"
}


def get_prices(url):
    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    prices = soup.find_all(
        "td",
        class_="text-left"
    )

    return [
        item.get_text(" ", strip=True)
        for item in prices
        if item.get_text(" ", strip=True)
    ]


print("=" * 60)
print("          TGJU FINAL TEST")
print("=" * 60)


# -------------------------
# تتر
# -------------------------

try:
    prices = get_prices(pages["تتر"])

    if len(prices) > 1:
        print(f"✅ تتر: {prices[1]}")
    else:
        print("❌ تتر: پیدا نشد")

except Exception as e:
    print(f"❌ تتر ERROR: {e}")


# -------------------------
# طلای 18
# -------------------------

try:
    prices = get_prices(pages["طلای 18 عیار"])

    print(f"✅ طلای 18 عیار: {prices[0]}")

except Exception as e:
    print(f"❌ طلای 18 عیار ERROR: {e}")


# -------------------------
# مثقال
# -------------------------

try:
    prices = get_prices(pages["مثقال طلا"])

    print(f"✅ مثقال طلا: {prices[0]}")

except Exception as e:
    print(f"❌ مثقال طلا ERROR: {e}")


# -------------------------
# سکه امامی
# -------------------------

try:
    prices = get_prices(pages["سکه امامی"])

    print(f"✅ سکه امامی: {prices[0]}")

except Exception as e:
    print(f"❌ سکه امامی ERROR: {e}")


# -------------------------
# نیم سکه
# -------------------------

try:
    prices = get_prices(pages["نیم سکه"])

    print(f"✅ نیم سکه: {prices[0]}")

except Exception as e:
    print(f"❌ نیم سکه ERROR: {e}")


# -------------------------
# ربع سکه
# -------------------------

try:
    prices = get_prices(pages["ربع سکه"])

    print(f"✅ ربع سکه: {prices[0]}")

except Exception as e:
    print(f"❌ ربع سکه ERROR: {e}")


# -------------------------
# انس جهانی
# -------------------------

try:
    prices = get_prices(pages["انس جهانی طلا"])

    print(f"✅ انس جهانی طلا: {prices[0]} دلار")

except Exception as e:
    print(f"❌ انس جهانی طلا ERROR: {e}")


print("=" * 60)
print("              TEST FINISHED")
print("=" * 60)
