from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr

# Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation_history = []

def chatbot_response(user_input):
    conversation_history.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history
    )

    reply = completion.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply})
    return reply

# Gradio Web UI
def gradio_chat(message, history):
    response = chatbot_response(message)
    return response

ui = gr.ChatInterface(
    fn=gradio_chat,
    title="🤖 AI ChatBot",
    description="A conversational chatbot powered by OpenAI API.",
)

if __name__ == "__main__":
    print("Launching Web UI...")
    ui.launch()
