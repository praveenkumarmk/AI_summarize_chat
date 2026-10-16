#prompt template
#model initialization
#chain initialization
#run the chain
#parse the result
#print the result

import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from scrapper import fetch_website_contents
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
prompt = ChatPromptTemplate.from_template(
    "Please summarize the website content: {website}",
)

model = ChatOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-120b",
    temperature=0.3,
)

parser = StrOutputParser()

chain = prompt | model | parser

def summarize_website(website_url):
 return chain.invoke({"website": fetch_website_contents(website_url)})

print(summarize_website("https://www.linkedin.com/feed/foryou/"));