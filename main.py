import os, time
import pandas as pd
from strategy import fetch_data, format_context
from ai_analysis import analyze_market_with_ai
from telegram import send_telegram_message

SYMBOLS = os.getenv("SYMBOLS", "ETHUSDT,BTCUSDT,SOLUSDT,XRPUSDT,FARTCOINUSDT").split(",")

def main():
    for symbol in SYMBOLS:
        df = fetch_data(symbol)
        context = format_context(symbol, df)
        ai_msg = analyze_market_with_ai(context)
        send_telegram_message(f"{symbol} 分析结果：\n{ai_msg}")
        time.sleep(1)

if __name__ == "__main__":
    main()
