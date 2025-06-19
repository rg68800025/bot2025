import os
from openai import OpenAI

# 初始化 OpenAI 客户端，使用环境变量中的 API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_with_ai(signal_text):
    try:
        # 调用 GPT-4 或 GPT-3.5 分析市场结构
        response = client.chat.completions.create(
            model="gpt-4",  # 可改为 "gpt-3.5-turbo" 以减少成本
            messages=[
                {
                    "role": "system",
                    "content": (
                        "你是一个专业的加密货币策略分析师，"
                        "请根据市场结构、成交量、VPVR 密集区进行简洁分析。"
                        "你的回复风格应直接、简明，适合推送给 Telegram 频道。"
                    )
                },
                {
                    "role": "user",
                    "content": signal_text
                }
            ],
            temperature=0.3,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[AI 分析失败] {str(e)}"
