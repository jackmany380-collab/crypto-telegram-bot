import os
import requests
from datetime import datetime, timezone

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@ZEROVIXX"

# دریافت قیمت BTC و ETH
url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

try:
    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    prices = response.json()

    btc_price = prices["bitcoin"]["usd"]
    btc_change = prices["bitcoin"]["usd_24h_change"]

    eth_price = prices["ethereum"]["usd"]
    eth_change = prices["ethereum"]["usd_24h_change"]

    btc_arrow = "🟢" if btc_change >= 0 else "🔴"
    eth_arrow = "🟢" if eth_change >= 0 else "🔴"

    now = datetime.now(timezone.utc)
    update_time = now.strftime("%Y-%m-%d %H:%M UTC")

    message = f"""📊 وضعیت بازار کریپتو

🟠 Bitcoin (BTC)
💰 قیمت: ${btc_price:,.2f}
{btc_arrow} تغییر 24h: {btc_change:+.2f}%

🔵 Ethereum (ETH)
💰 قیمت: ${eth_price:,.2f}
{eth_arrow} تغییر 24h: {eth_change:+.2f}%

🕐 آخرین بروزرسانی:
{update_time}

━━━━━━━━━━━━━━
🤖 Crypto Bot
"""

    # ارسال به تلگرام
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL,
        "text": message
    }

    telegram_response = requests.post(
        telegram_url,
        data=data,
        timeout=20
    )

    print("Telegram Status:", telegram_response.status_code)
    print("Telegram Response:", telegram_response.text)

except Exception as e:
    print("❌ Error:", e)
    raise
