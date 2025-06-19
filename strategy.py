import requests, pandas as pd

def fetch_data(symbol):
    url = f"https://api.bitget.com/api/v2/market/candles?symbol={symbol}&granularity=3600"
    data = requests.get(url).json().get("data", [])
    df = pd.DataFrame(data, columns=["ts","open","high","low","close","vol"])
    df = df.rename(columns={"vol":"volume", "ts":"timestamp"})
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)
    return df

def format_context(symbol, df):
    last = df.iloc[-5:].describe().to_dict()
    return f"SYMBOL={symbol}, last 5 bar close stats: {last}"
