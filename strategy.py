import pandas as pd

def run_strategy():
    data = {
        "symbol": ["ETHUSDT", "BTCUSDT"],
        "signal": ["short", "long"],
        "entry": [2536.29, 67890],
        "stop": [2575, 66666],
        "target": [2450, 70000]
    }
    df = pd.DataFrame(data)
    return df
