# 🤖 Smart AI Assistant

A local AI chatbot built with **Streamlit**, **Ollama**, and **Llama 3.2**. It provides intelligent conversational responses while running completely on your local machine.

## 🚀 Features

- 💬 Interactive AI Chat Interface
- 🤖 Powered by Llama 3.2
- ⚡ Local inference using Ollama
- 🔒 Privacy-friendly (runs locally)
- 📝 Conversation history
- 🗑️ Clear chat functionality
- 🎨 Clean and responsive Streamlit UI

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama
- Llama 3.2

## 📂 Project Structure

```
Smart-AI-Assistant/
│
├── pages/
│   └── Chatbot.py
│
├── src/
│   ├── chat.py
│   ├── constants.py
│   └── utils.py
│
├── logs/
├── Welcome.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/keyurnanera1945-a11y/Smart-AI-Assistant.git
```

Move into the project folder:

```bash
cd Smart-AI-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama serve
```

Download the model:

```bash
ollama pull llama3.2
```

Run the application:

```bash
streamlit run Welcome.py
```

## 👨‍💻 Author

**Keyur Nanera**

GitHub: https://github.com/keyurnanera1945-a11y
