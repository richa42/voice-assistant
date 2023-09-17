import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am richi. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def get_weather(location):
    url = f'https://www.weather.com/weather/today/l/{location}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        weather_info = soup.find('div', class_='CurrentConditions--primary--2DOqs')
        temperature = weather_info.find('span', class_='CurrentConditions--tempValue--3KcTQ').text
        condition = weather_info.find('div', class_='CurrentConditions--phraseValue--2xXSr').text
        return f"The current temperature in {location} is {temperature} and the weather condition is {condition}."
    except Exception as e:
        return "Could not fetch weather information."

def system_action(action):
    if "shutdown" in action:
        os.system("shutdown /s /t 0")
    elif "restart" in action:
        os.system("shutdown /r /t 0")
    elif "log off" in action or "logoff" in action:
        os.system("shutdown -l")

def search_on_youtube(query):
    query = query.replace("search on YouTube", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            speak('Say the song name...')
            song = takeCommand().lower()
            search_on_youtube(song)
            print(results)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\richa\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'weather' in query:
            speak("Sure, please tell me the city or location name.")
            city = takeCommand().lower()
            weather_info = get_weather(city)
            speak(weather_info)

        elif 'shutdown' in query or 'restart' in query or 'log off' in query:
            system_action(query)
        
        
