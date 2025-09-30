# Groq AI Chatbot

A simple **multi-chat AI-powered chatbot** built with **Streamlit** and the **Groq API**.  
Supports multiple chat sessions, in-memory chat history, and dynamic chat titles.

---

## Features

- Multi-turn conversation with AI
- Multiple chat sessions in the sidebar
- Dynamic chat titles based on first user message
- Create new chats with a single click
- In-memory chat history (resets on page refresh)
- Easy to run locally with environment variable for API key

---

## Requirements

- Python 3.10+
- Groq API Key
- Packages listed in `requirements.txt`

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/groq-ai-chatbot.git
cd groq-ai-chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

---

## Usage

Run the chatbot locally:

```bash
streamlit run chatbot.py
```

- Open the URL provided by Streamlit (usually `http://localhost:8501`)
- Use the sidebar to create or switch chats
- Type messages in the chat input box
- The first user message automatically sets the chat title

---

## Project Structure

```
groq-ai-chatbot/
├─ chatbot.py        # Main Streamlit app
├─ requirements.txt  # Python dependencies
├─ .env              # Environment variables (API key)
└─ README.md         # Project documentation
```

---

## Environment Variables

- `GROQ_API_KEY` → Your free Groq API key for AI inference

---

## Future Enhancements

- Add persistent storage (Redis or database) for chat history
- Add ability to delete chat sessions
- Editable chat titles via pencil icon (like ChatGPT)
- UI improvements and mobile-friendly layout
