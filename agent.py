import json
from openai import OpenAI

from summarize_langchain import GROQ_API_KEY

client = OpenAI();

PRICES = {"shoes": 799, "shirt": 800, "pant": 300, "innerwear": 200}

#define tool to answer Chat question, here Every function is tool
def get_price(item):
    print(f"tool called get_price({item})");
    return f"price of {item} $ {PRICES.get({item})}"

# Define tool, may AI model get to know whether function exist

tools = [{ "type": "function",
            "function": {
                "name": "get_price",
                "description": "This function used to read price of item passed",
                "parameters": {
                    "type": "object",
                    "properties": {"item": {"type": "string", "description": "the item name"}},
                    "required": ["item"],
                },

            }
        }
    ]

def agent(userMessage): 
        messages = [{"role": "user", "content": userMessage}];
        response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, tools=tools)
        msg = response.choices[0].message
        #print(f'{msg}');

        #did it ask for tool
        if msg.tool_calls:
         messages.append(msg)
         for call in msg.tool_calls:
            args = json.loads(call.function.arguments)   # 3. read its request...
            result = get_price(args["item"])             #    ...and run the real function
            messages.append({
                "role": "tool",                          # a third role!
                "tool_call_id": call.id,
                "content": result,
            })
        # 4. send everything back so it can answer nicely
        response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        msg = response.choices[0].message

        return msg.content

if __name__ == "__main__":
    print(agent("How much are the shoes?"))       # -> uses the tool -> "₹799"
    print(agent("Hi! What can you help with?"))    # -> no tool needed -> just chats