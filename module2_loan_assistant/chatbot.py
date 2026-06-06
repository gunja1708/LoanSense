# Module 2 — Loan AI Assistant
# chatbot.py — Bilingual Hindi + English loan chatbot

from google import genai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# System context for loan assistant
SYSTEM_PROMPT = """
You are LoanSense — an expert AI loan assistant for Indian borrowers.
You answer questions about:
- Loan eligibility
- EMI calculations
- Bank comparisons (SBI, HDFC, ICICI)
- Document requirements
- Interest rates

You respond in the same language the user writes in.
If they write in Hindi, respond in Hindi.
If they write in English, respond in English.
Keep answers simple, clear and helpful.
"""

def chat(user_message):
    """
    Sends user message to Gemini and returns response.
    """
    try:
        full_prompt = SYSTEM_PROMPT + "\nUser: " + user_message
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=full_prompt
        )
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⚠️ Free tier quota exceeded for today. Please try again tomorrow or create a new API key at aistudio.google.com"
        else:
            return f"❌ Error: {str(e)}"


def main():
    """
    Main loop — keeps chatbot running until user types 'exit'.
    """
    print("🏦 Welcome to LoanSense AI Assistant!")
    print("💬 Ask me anything about loans in Hindi or English.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Thank you for using LoanSense!")
            break

        if user_input.strip() == "":
            continue

        print("\n🤖 LoanSense: ", end="")
        response = chat(user_input)
        print(response)
        print()


if __name__ == "__main__":
    main()