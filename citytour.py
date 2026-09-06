import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url = "https://api.groq.com/openai/v1"
    )
messages = [{"role": "system", "content": "I am funny traveler?"},
                {"role": "user", "content": "Which is the best place to visit in the bengaluru?"}]
response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

print(response.choices[0].message.content)