import os
from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_with_ai(prompt: str) -> str:
    """
    使用 OpenAI GPT-4 分析市场文本数据。

    参数:
        prompt (str): 提示内容，例如行情数据、结构判断等

    返回:
        str: AI 返回的策略分析结果
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "你是一个专业的加密货币交易员，请根据提示分析行情并给出清晰逻辑。"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI分析失败: {str(e)}"
