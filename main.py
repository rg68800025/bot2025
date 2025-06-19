from strategy import run_strategy
from telegram import send_telegram_message
from ai_analysis import analyze_with_ai

if __name__ == "__main__":
    result = run_strategy()
    ai_summary = analyze_with_ai(result)
    send_telegram_message(ai_summary)
