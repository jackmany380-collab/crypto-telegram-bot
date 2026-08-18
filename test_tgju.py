import requests

URL = "https://www.tgju.org/"

try:
    response = requests.get(
        URL,
        timeout=20,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("Status:", response.status_code)
    print("Length:", len(response.text))

    if response.status_code == 200:
        print("✅ TGJU قابل دسترسی است")
    else:
        print("❌ TGJU پاسخ عادی نداد")

except Exception as e:
    print("❌ ERROR:", e)
