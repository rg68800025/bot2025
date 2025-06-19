import os, openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_market_with_ai(context):
    prompt = f"""
你是威科夫结构分析+量价动能专家。
请根据如下行情结构描述，判断当前是否适合做多、做空或观望，并提供止盈止损建议：
{context}
"""
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2,
        max_tokens=200
    )
    return resp["choices"][0]["message"]["content"].strip()
