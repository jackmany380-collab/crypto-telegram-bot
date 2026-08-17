import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@نام_کاربری_کانال"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHANNEL,
    "text": "🎉 تست موفق!\n\nربات با موفقیت به کانال متصل شد."
}

response = requests.post(url, data=data, timeout=20)

print("Status:", response.status_code)
print("Response:", response.text)
