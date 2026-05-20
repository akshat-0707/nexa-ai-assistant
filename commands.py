import webbrowser
import musicLibrary
import requests
from speak import speak
from client import ai_process
from datetime import datetime
import  os
import speech_recognition as sr
import psutil 

r = sr.Recognizer()
news_api =  os.getenv("News_Api")

def date_time():
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        today = datetime.now().strftime("%d %B %Y")
        speak(today)
        speak(f"current time: {current_time}")

def add_task():
        # check if task.txt exists and create one if not
        if not os.path.exists("tasks.txt"):
            with open ("tasks.txt", "w") as f:
                f.write(" ")
        # Listen for task
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("adding task...")
            audio = r.listen(source, timeout=4, phrase_time_limit=3)
            new_task = r.recognize_google(audio)
        # Write the task in the .txt file in new line
        with open ("tasks.txt", "a") as f:
            f.write(new_task + "\n")

def access_tasks():
    # check if tasks.txt exists 
    if not os.path.exists("tasks.txt"):
        speak("file not found")
        return
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    # check if file is empty
    if len(lines) == 0:
        speak("no tasks")
        return
    # speak all tasks with serial number
    for line_num, line in enumerate(lines, start=1):
        speak(f"task number {line_num} is {line}")


def remove_task():
        speak("Sure, provide me the serial number of the task you want removed")
        # listen for the task number
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("listening for serialno....")
            audio = r.listen(source, timeout=4, phrase_time_limit=3)
        command = r.recognize_google(audio)
        # to check if user provided command is int only
        try:
            task_index = int(command)
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
            if task_index < 1 or task_index > len(lines):
                speak("invalid task number")
                return
            try: # to check if theres any task at the user provided serial no.
                with open ("tasks.txt", "w") as f:
                    for line_num, line in enumerate(lines, start=1):
                        if line_num != task_index:
                            f.write(line)
                    speak(f"task number {task_index} removed successfully")
            except: speak("there is no task at the provided serial number")
        except: speak("speak the serial number only")

def write_note():
        # to check if note file exists
        if not os.path.exists("note.txt"):
            with open ("note.txt", "w") as f:
                f.write(" ")
        #listen for command
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("taking note...")
            audio = r.listen(source, timeout=4, phrase_time_limit=3)
            command_note = r.recognize_google(audio)
        # Write the command in new line
        with open ("note.txt", "a") as f:
            f.write(command_note + "\n")

def access_note():
        # Check if the file exists
        if not os.path.exists("note.txt"):
            speak("file not found")
            return
        with open ("note.txt") as f:
            content = f.read()
        if content.strip() == "":
            speak("notes are empty")
        else: speak(content)

def processCommand(c):
    c = c.lower()
    if ("open google" in c):
        webbrowser.open("https://google.com")

    elif ("open linkedin" in c):
        webbrowser.open("https://in.linkedin.com/")

    elif ("open instagram" in c):
        webbrowser.open("https://instagram.com")

    elif ("open youtube" in c):
        webbrowser.open("https://youtube.com")

    elif (c.startswith("play")):
        found = False
        for key in musicLibrary.music:
            song = c.replace("play", "").strip()
            if song.lower() == key.lower():
                link = musicLibrary.music[key]
                webbrowser.open(link)
                found = True
                break
        if not found : speak ("song not found")

    elif ("news" in c):
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
        data = response.json()
        if "articles" in data:
            for article in data["articles"]:
                speak(article["title"])
                print(article["title"])
        else:
            speak("Unable to fetch news")
    
    elif "battery percentage" in c:
        battery = psutil.sensors_battery()
        percent = battery.percent
        speak(f"Battrey is at {percent} percent")

    elif ("take note" in c) or ("take a note" in c):
        speak("sure!")
        print("sure")  # this too is temporary 
        write_note()

    elif ("add task") in c:
        add_task()

    elif ("read task") in c:
        access_tasks()

    elif ("remove task" in c):
         remove_task()
    
    elif "read notes" in c or "read note" in c:
        access_note()

    elif ("date" in c) or ("time" in c):
        date_time()

    elif "bye" in c:
        speak("Bye, have a nice day")
        exit()

    else:  #let Gemini handle the request
        output = ai_process(c)
        speak(output)
        print(output)