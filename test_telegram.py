import os, requests
from dotenv import load_dotenv

load_dotenv()  # 讀 .env

token = os.getenv("TELEGRAM_BOT_TOKEN")
chat  = os.getenv("TELEGRAM_CHAT_ID")
assert token and chat, "環境變數沒載到"

r = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={"chat_id": chat, "text": "test_telegram.py 測試訊息 ✅"},
    timeout=10
)
print(r.status_code, r.text)
