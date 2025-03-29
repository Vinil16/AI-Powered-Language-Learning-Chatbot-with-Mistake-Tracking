import google.generativeai as genai
import sqlite3
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Set GOOGLE_API_KEY as an environment variable.")

genai.configure(api_key=API_KEY)
# Choose a supported Gemini model
MODEL_NAME = "gemini-1.5-pro-latest"  # Updated to the latest stable model

def setup_database():
    """Creates the database if it does not exist to track user mistakes."""
    conn = sqlite3.connect("mistakes.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mistakes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        correction TEXT,
        explanation TEXT
    )""")
    conn.commit()
    conn.close()

def log_mistake(user_input, correction, explanation):
    """Logs user mistakes into the SQLite database."""
    conn = sqlite3.connect("mistakes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mistakes (user_input, correction, explanation) VALUES (?, ?, ?)", 
                   (user_input, correction, explanation))
    conn.commit()
    conn.close()

def generate_final_review():
    """Generates a summary of recorded mistakes."""
    conn = sqlite3.connect("mistakes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_input, correction, explanation FROM mistakes")
    mistakes = cursor.fetchall()
    conn.close()
    
    if not mistakes:
        return "No mistakes recorded. Well done! 🎉"
    
    review = "📖 **Final Review of Mistakes:**\n"
    for mistake in mistakes:
        review += f"\n🔹 **User Input:** {mistake[0]}\n✅ **Correction:** {mistake[1]}\nℹ️ **Explanation:** {mistake[2]}\n"
    
    return review

def chat_with_user(known_lang, learning_lang, level):
    """Handles conversation with the AI model and tracks mistakes."""
    model = genai.GenerativeModel(MODEL_NAME)
    
    print(f"\n🌍 Chatbot is ready! Type 'exit' to stop.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("\n", generate_final_review())
            break

        prompt = (
            f"You are a language tutor. The user knows {known_lang} and is learning {learning_lang} "
            f"at a {level} level. Respond in {learning_lang} and correct mistakes if any."
        )

        try:
            response = model.generate_content(prompt + "\nUser: " + user_input)
            response_text = response.text.strip()

            # Check if there's a mistake (basic check, can be improved)
            if "mistake" in response_text.lower() or "correction" in response_text.lower():
                correction = "Example correction for: " + user_input
                explanation = "This is a placeholder explanation for the mistake."
                log_mistake(user_input, correction, explanation)
                print(f"\n✅ Correction: {correction}\nℹ️ Explanation: {explanation}")

            print(f"\n🤖 Bot ({learning_lang}): {response_text}")

        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    setup_database()
    known_lang = input("Enter your known language: ")
    learning_lang = input("Enter the language you want to learn: ")
    level = input("Enter your proficiency level (Beginner/Intermediate/Advanced): ")
    chat_with_user(known_lang, learning_lang, level)
