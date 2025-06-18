from src.strategy import analyze_market
from utils.telegram import send_telegram_message

if __name__ == "__main__":
    signal = analyze_market()
    if signal:
        send_telegram_message(signal)
