from flask import Flask, request
import os
import requests
from telegram import Bot

app = Flask(__name__)
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == "/status":
            bot.send_message(chat_id=chat_id, text="🟢 系统在线，狙击策略运行中")
        elif text == "/trigger":
            from main import run_strategy  # 假设 main.py 中有 run_strategy 方法
            result = run_strategy()
            bot.send_message(chat_id=chat_id, text=f"📊 策略已触发：{result}")
        else:
            bot.send_message(chat_id=chat_id, text="🤖 请输入 /status 或 /trigger")
    return "ok", 200
