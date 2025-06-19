import os
from openai import OpenAI

def test_ai():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY 没有配置")
        return

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": "用一句话总结以太坊当前市场情绪"},
            ],
        )
        print("✅ 成功响应：", response.choices[0].message.content)
    except Exception as e:
        print("❌ 出错：", str(e))

if __name__ == "__main__":
    test_ai()
