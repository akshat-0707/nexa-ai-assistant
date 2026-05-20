import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

gemini_api = os.getenv("Gemini_Api")

def ai_process(command):
    client = genai.Client(api_key=gemini_api)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=command,
        config={
            "system_instruction": "You are Nexa, a helpful AI assistant like Alexa or Siri. Keep responses short, clear, and conversational."
        }
    )

    return (response.text)
