# Nexa

A voice-controlled AI assistant built with Python.

Nexa can listen to voice commands, respond using Google's Gemini API, manage notes/tasks, read news headlines, open websites, play music, and perform small desktop assistant tasks through natural voice interaction.

## Features

- Voice recognition
- AI responses using Gemini API
- Text-to-speech replies
- Open websites with voice commands
- Play music from custom library
- Notes system
- Task manager
- News headlines
- Battery percentage checker
- Date & time support
- Modular code structure

## Tech Used

- Python
- SpeechRecognition
- PyAudio
- Google Gemini API
- gTTS
- pygame
- requests
- python-dotenv

## Installation

Clone the repository:

```bash
git clone https://github.com/akshat-0707/nexa-ai-assistant.git
cd nexa-ai-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
Gemini_Api=YOUR_API_KEY
News_Api=YOUR_API_KEY
```

Run the assistant:

```bash
python main.py
```

## Example Commands

- "Open YouTube"
- "Play music"
- "Take note"
- "Read notes"
- "Add task"
- "Remove task"
- "Battery percentage"
- "Tell me the news"

## Project Structure

```text
main.py            # Main assistant loop
commands.py        # Voice command handling
client.py          # Gemini API integration
speak.py           # Text-to-speech
musicLibrary.py    # Music database
```

## About

Built as a learning project while exploring Python, APIs, automation, and AI integrations.
