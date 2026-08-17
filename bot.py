print("ربات کریپتو شروع شد!")

import requests

print("در حال تست اتصال...")

response = requests.get(
    "https://api.telegram.org",
    timeout=20
)

print("Status:", response.status_code)
print("اتصال برقرار شد!")
