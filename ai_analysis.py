import openai
import os

def analyze_with_ai(df):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    text = df.to_string()
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"请分析以下交易信号并总结：\n{text}"}]
    )
    return response.choices[0].message.content
