import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="openai/gpt-oss-120b",
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "I am funny traveler?"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | llm

# One in-memory history per session_id, so multiple conversations don't mix.
store = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chat_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

session_id = "test-session-1"
config = {"configurable": {"session_id": session_id}}

response1 = chat_with_history.invoke(
    {"input": "Which is the best place to visit in the bengaluru?"},
    config=config,
)
print("AI:", response1.content)

# Follow-up question relies on chat history to know what "it" refers to.
response2 = chat_with_history.invoke(
    {"input": "What is the best time of year to visit it?"},
    config=config,
)
print("AI:", response2.content)

print("\n--- Full history for session:", session_id, "---")
for message in get_session_history(session_id).messages:
    print(f"{message.type}: {message.content}")
