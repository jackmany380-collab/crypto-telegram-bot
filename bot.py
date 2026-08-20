import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone


# =========================================================
# تنظیمات
# =========================================================

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@ZEROVIXX"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# =========================================================
# دریافت قیمت BTC و ETH
# =========================================================

def get_crypto_prices():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    prices = response.json()

    btc_price = prices["bitcoin"]["usd"]
    btc_change = prices["bitcoin"]["usd_24h_change"]

    eth_price = prices["ethereum"]["usd"]
    eth_change = prices["ethereum"]["usd_24h_change"]

    return (
        btc_price,
        btc_change,
        eth_price,
        eth_change
    )


# =========================================================
# دریافت قیمت‌های TGJU
# =========================================================

def get_tgju_prices():

    pages = {
        "tether": "https://www.tgju.org/profile/crypto-tether",
        "gold18": "https://www.tgju.org/profile/geram18",
        "mesghal": "https://www.tgju.org/profile/mesghal",
        "coin": "https://www.tgju.org/profile/sekee",
        "half": "https://www.tgju.org/profile/nim",
        "quarter": "https://www.tgju.org/profile/rob",
        "ounce": "https://www.tgju.org/profile/ons"
    }

    results = {}

    for name, url in pages.items():

        try:

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=20
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            prices = soup.find_all(
                "td",
                class_="text-left"
            )

            values = [
                item.get_text(" ", strip=True)
                for item in prices
                if item.get_text(" ", strip=True)
            ]

            # -------------------------------------------------
            # تتر
            # قیمت فعلی تتر در index شماره 1
            # -------------------------------------------------

            if name == "tether":

                if len(values) > 1:
                    results[name] = values[1]
                else:
                    results[name] = "نامشخص"

            # -------------------------------------------------
            # سایر قیمت‌ها
            # قیمت فعلی در index شماره 0
            # -------------------------------------------------

            else:

                if len(values) > 0:
                    results[name] = values[0]
                else:
                    results[name] = "نامشخص"

        except Exception as e:

            print(f"TGJU Error - {name}: {e}")

            results[name] = "نامشخص"

    return results


# =========================================================
# دریافت دلار آزاد
# =========================================================

def get_dollar():

    try:

        # صفحه مستقیم دلار آزاد TGJU
        url = "https://www.tgju.org/profile/price_dollar_rl"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        prices = soup.find_all(
            "td",
            class_="text-left"
        )

        values = [
            item.get_text(" ", strip=True)
            for item in prices
            if item.get_text(" ", strip=True)
        ]

        # قیمت فعلی دلار = index 0
        if len(values) > 0:
            return values[0]

        return "نامشخص"

    except Exception as e:

        print("Dollar Error:", e)

        return "نامشخص"


# =========================================================
# ساخت پیام
# =========================================================

def build_message():

    print("🚀 شروع دریافت اطلاعات...")

    # -----------------------------------------------------
    # کریپتو
    # -----------------------------------------------------

    btc_price, btc_change, eth_price, eth_change = (
        get_crypto_prices()
    )

    btc_arrow = "🟢" if btc_change >= 0 else "🔴"
    eth_arrow = "🟢" if eth_change >= 0 else "🔴"

    # -----------------------------------------------------
    # TGJU
    # -----------------------------------------------------

    print("📡 دریافت اطلاعات TGJU...")

    tgju = get_tgju_prices()

    # -----------------------------------------------------
    # دلار آزاد
    # -----------------------------------------------------

    print("💵 دریافت دلار آزاد...")

    dollar = get_dollar()

    # -----------------------------------------------------
    # زمان
    # -----------------------------------------------------

    now = datetime.now(timezone.utc)

    update_time = now.strftime(
        "%Y-%m-%d %H:%M UTC"
    )

    # -----------------------------------------------------
    # پیام نهایی
    # -----------------------------------------------------

    message = f"""📊 وضعیت بازار

🪙 کریپتو

🟠 Bitcoin (BTC)
💰 قیمت: ${btc_price:,.2f}
{btc_arrow} تغییر 24h: {btc_change:+.2f}%

🔵 Ethereum (ETH)
💰 قیمت: ${eth_price:,.2f}
{eth_arrow} تغییر 24h: {eth_change:+.2f}%

━━━━━━━━━━━━━━

💵 بازار ارز

🇺🇸 دلار آزاد: {dollar} تومان
💲 تتر: {tgju["tether"]} تومان

━━━━━━━━━━━━━━

🥇 بازار طلا

🔸 طلای ۱۸ عیار: {tgju["gold18"]} تومان
⚖️ مثقال طلا: {tgju["mesghal"]} تومان
🌕 انس جهانی: ${tgju["ounce"]}

━━━━━━━━━━━━━━

🪙 سکه

👑 سکه امامی: {tgju["coin"]} تومان
🟡 نیم‌سکه: {tgju["half"]} تومان
🟠 ربع‌سکه: {tgju["quarter"]} تومان

━━━━━━━━━━━━━━

🕐 آخرین بروزرسانی:
{update_time}

#بیتکوین #اتریوم #دلار #تتر #طلا #سکه

📢 @zerovixx
"""

    return message


# =========================================================
# ارسال پیام به تلگرام
# =========================================================

try:

    message = build_message()

    print("\n========== MESSAGE ==========\n")
    print(message)
    print("\n==============================\n")

    telegram_url = (
        f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    )

    data = {
        "chat_id": CHANNEL,
        "text": message
    }

    telegram_response = requests.post(
        telegram_url,
        data=data,
        timeout=20
    )

    print(
        "Telegram Status:",
        telegram_response.status_code
    )

    print(
        "Telegram Response:",
        telegram_response.text
    )

    telegram_response.raise_for_status()

    print("✅ پیام با موفقیت ارسال شد!")

except Exception as e:

    print("❌ Error:", e)

    raise
