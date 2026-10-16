import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from summarize_langchain import prompt

prompt = ChatPromptTemplate.from_messages([
  ("system", "You are friendly tutor"),
  MessagesPlaceholder("history"),
  ("human", "{question}")
]);
load_dotenv();
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
model = ChatOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-120b",
    temperature=0.3,
)

history = [HumanMessage("My name is aarav"), AIMessage("Hi Aarav")];
chain = prompt | model | StrOutputParser();
print(chain.invoke({"history": history, "question": "What's my name?"}));