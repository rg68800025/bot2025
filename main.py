from flask import Flask, request
import os
from strategy import run_strategy
from telegram import send_telegram_message
from ai_analysis import analyze_with_ai
from telegram import Bot

app = Flask(__name__)
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))

# ✅ Webhook 入口
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == "/status":
            bot.send_message(chat_id=chat_id, text="✅ 系统在线，狙击策略部署成功")
        elif text == "/trigger":
            result = run_strategy()
            ai_summary = analyze_with_ai(result)
            bot.send_message(chat_id=chat_id, text=f"🎯 策略触发结果：\n{ai_summary}")
        else:
            bot.send_message(chat_id=chat_id, text="🤖 支持指令：/status /trigger")
    return "ok", 200

# ✅ 启动入口（支持 Railway 自动运行）
if __name__ == "__main__":
    # 也可用作计划任务触发时运行
    result = run_strategy()
    ai_summary = analyze_with_ai(result)
    send_telegram_message(ai_summary)

    # 同时开启 Web 服务
    app.run(host="0.0.0.0", port=8000)
