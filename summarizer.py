import os
from openai import OpenAI
from dotenv import load_dotenv

from scrapper import fetch_website_contents

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def summarize_website(url):
    website = fetch_website_contents(url)

    messages = [
        {"role": "system", "content": "You summarize webpages clearly and concisely for a reader in a hurry."},
        {"role": "user", "content": f"summarize the following website: {website}"},
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    return response.choices[0].message.content
