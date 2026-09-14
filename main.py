import speech_recognition as sr
from dotenv import load_dotenv
from commands import processCommand
from speak import speak
from client import ai_process

load_dotenv()
recognizer = sr.Recognizer()

'''def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()'''

if __name__ == "__main__":
    speak("Initializing Nexa.....")
    while True:
    # obtain audio from the microphone
        r = recognizer
        print("Recognizing...") 

    # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)

    # Listen for the wake word "nexa"
            wake_words = ["nexa", "next", "nexus", "alexa"]
            if any(w in word.lower() for w in wake_words):
                speak("ya")
                print("ya")  # optional: print to console for debugging
    #listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Nexa active...")
                    audio = r.listen(source, timeout=8, phrase_time_limit=8)
                    command = r.recognize_google(audio)
                    processCommand(command)


        except sr.UnknownValueError:
            print("Nexa could not understand audio")
        except sr.WaitTimeoutError:
            print("Listening timeout")
        except Exception as e:
            print(f"error: {e}")
