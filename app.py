import gradio as gr
from agent import agent
import summarizer


def chat(message, history):
    # Gradio fills in `message` (newest) and `history` (past turns) for you.
    # Homework hint: pass `history` into your agent to give it memory!
    return agent(message)

# gr.Interface(
#     fn=summarizer.summarize_website,                                  # your function
#     inputs=gr.Textbox(label="Website URL"),
#     outputs=gr.Markdown(label="Summary"),
#     title="🔎 AI Website Summarizer",
# ).launch(share=True)   # share=True → a public link you can post! 🎉

gr.ChatInterface(
 fn=chat,
 title="Shopping chat",
 description="Ask me the price of shoes, hat, bag, shorts or pants — I'll look it up.",
).launch(share=True)



