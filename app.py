import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Load resume
with open("resume.txt", "r", encoding="utf-8") as f:
    knowledge_base = f.read()

def ask_question(question):

    prompt = f"""
Answer ONLY using the context below.
If answer not found say "I don't know".

Context:
{knowledge_base}

Question:
{question}
"""

    payload = {
        "model": "openrouter/auto",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        result = response.json()

        # DEBUG if API returns error
        if "choices" not in result:
            return str(result)

        answer = result["choices"][0]["message"]["content"]

        return answer

    except Exception as e:
        return str(e)


while True:
    q = input("\nAsk (type exit): ")

    if q.lower() == "exit":
        break

    print("\n", ask_question(q))