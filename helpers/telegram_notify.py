# helpers/telegram_notify.py
import os, requests
from dotenv import load_dotenv

load_dotenv()  # 保險起見

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(text: str) -> bool:
    if not BOT_TOKEN or not CHAT_ID:
        print(f"[telegram] 未設定 BOT_TOKEN/CHAT_ID，略過。BOT_TOKEN={bool(BOT_TOKEN)} CHAT_ID={CHAT_ID!r}")
        return False
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, json={"chat_id": CHAT_ID, "text": text}, timeout=10)
        if resp.status_code != 200:
            print(f"[telegram] 送出失敗: {resp.status_code} {resp.text}")
            return False
        data = resp.json()
        if not data.get("ok"):
            print(f"[telegram] API 回傳 ok=false: {data}")
            return False
        return True
    except Exception as e:
        print(f"[telegram] 例外: {e}")
        return False
