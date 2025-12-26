import requests

def generate_ai_explanation(stock_data: dict):
    try:
        prompt = f"""
You are a financial market explainer.

STRICT RULES:
- Respond in **maximum 2 sentences**
- Do NOT use headings or labels
- Do NOT say "here is an explanation" and use bullet points
- Do NOT give investment advice
- Do NOT predict future prices
- Use observational and uncertain language

Observed data:
- Stock: {stock_data['symbol']}
- Price change: {stock_data['percent_change']}%
- Volume: {stock_data['volume']}

Write a concise explanation in plain text.
End with a short uncertainty disclaimer.
"""


        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:8b",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        return response.json()["response"].strip()

    except Exception as e:
        print("Local AI Error:", e)
        return "AI explanation temporarily unavailable."
