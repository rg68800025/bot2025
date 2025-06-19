import os, requests

def send_telegram_message(msg):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat = os.getenv("TELEGRAM_CHAT_ID")
    print(f"[BOT] 正在发送消息: {msg}")

    if token and chat:
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": chat, "text": msg}
        )
        print(f"[BOT] 响应: {response.status_code} - {response.text}")
    else:
        print("[BOT] 环境变量未设置完整")
