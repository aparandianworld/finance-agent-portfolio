import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "user", "content": "In the context of AI/ML, what are agents? Please provide a brief explanation."}
    ]
)
print(response.choices[0].message.content)