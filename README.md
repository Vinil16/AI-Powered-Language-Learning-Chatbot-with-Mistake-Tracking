# 🧠 AI-Powered Language Learning Chatbot with Mistake Tracking

This project is a smart, interactive chatbot designed to help users improve their language skills. It uses **OpenAI** and **Gemini API** to hold intelligent conversations, tracks user mistakes, and gives real-time feedback to accelerate learning. Built using **LangChain**, **Streamlit**, and **SQLite**, it’s a powerful assistant for anyone learning a new language.

---

## 🚀 Features

- ✨ **Conversational AI**: Human-like conversations powered by OpenAI and Gemini.
- 🧩 **Mistake Tracking**: Identifies grammar or vocabulary mistakes in real-time.
- 📈 **Progress Monitoring**: Stores user responses and provides feedback over time.
- 🗂️ **Contextual Memory**: Keeps chat context to deliver relevant responses.
- 💬 **Multi-turn Dialogue**: Smooth and continuous interactions.
- 🖥️ **Streamlit UI**: Simple and responsive frontend for user interaction.
- 🛠️ **SQLite Integration**: Local database to store user conversations and errors.

---

## 📁 Project Structure

```bash
├── app.py                        # Main Streamlit app
├── chatbot.py                    # Core chatbot logic
├── feedback.py                   # Mistake detection and feedback generation
├── db.py                         # SQLite database handling
├── utils.py                      # Helper functions
├── requirements.txt              # Required dependencies
├── README.md                     # Project documentation
└── data/
    └── chatbot.db                # SQLite database file
