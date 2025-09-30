import os
import requests
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(messages):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": messages,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.text}"

st.set_page_config(page_title="Groq AI Chatbot", page_icon="🤖")
st.title("🤖 Groq AI Chatbot with Multiple Chats")

if "chats" not in st.session_state:
    st.session_state.chats = {}
if "current_chat" not in st.session_state:
    chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.current_chat = chat_id
    st.session_state.chats[chat_id] = {
        "title": "Chat at " + chat_id,
        "messages": [{"role": "system", "content": "You are a helpful AI assistant."}]
    }

with st.sidebar:
    st.subheader("💬 Chat History")
    if st.button("➕ New Chat"):
        chat_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.current_chat = chat_id
        st.session_state.chats[chat_id] = {
            "title": "Chat at " + chat_id,
            "messages": [{"role": "system", "content": "You are a helpful AI assistant."}]
        }
    for chat_id, chat_data in st.session_state.chats.items():
        if st.button(chat_data["title"], key=chat_id):
            st.session_state.current_chat = chat_id

chat_id = st.session_state.current_chat
chat_data = st.session_state.chats[chat_id]
messages = chat_data["messages"]

for msg in messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])

if prompt := st.chat_input("Type your message..."):
    messages.append({"role": "user", "content": prompt})
    if chat_data["title"].startswith("Chat at"):
        chat_data["title"] = " ".join(prompt.split()[:5]) + ("..." if len(prompt.split()) > 5 else "")
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_groq(messages)
            st.write(response)
    messages.append({"role": "assistant", "content": response})
    st.session_state.chats[chat_id]["messages"] = messages
