import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import os
import random
import pyautogui



engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    speak("Hello how are you Aannikket")
    speak("I am MAAHI")
    
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour <18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening")
    speak(" How can I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold =100000
        audio=r.listen(source)

    try:
        print("Recognizing ....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
        return query

    except Exception as e:
        print("I cant hear this please Say that Again")
        return "none"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
       query =takeCommand().lower()

       if  'wikipedia' in query:
           speak('searching wikipedia......')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           speak(results)
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")  
       elif 'open spotify' in query:
           webbrowser.open("spotify.com")
       elif 'play my favorite song' in query:
           webbrowser.open("https://www.youtube.com/watch?v=eKu1YjaEoV0&list=RDeKu1YjaEoV0&start_radio=1")
        
       elif 'play music' in query:
           music_dir = 'C:\\Users\\anike\\Pictures\Music'
           songs = os.listdir(music_dir)
           os.startfile(os.path.join(music_dir,songs[0]))

       elif ' open vlc player' in query:
           openpath = "C:\\Users\Public\\Desktop\\VLC media player.lnk" 
           os.startfile(openpath)
       elif ' play movies' in query:
           mvOpen = "C:\\Users\\anike\\Pictures\\MOVIES\\Bhagam Bhag 2006 (HD) - Full Movie - Superhit Comedy Movie - Akshay Kumar - Govinda -  Paresh Rawal.mp4"
           os.startfile(mvOpen)
        
       elif 'search' in query:
           speak("searching....")
           ds = query.replace('search','')
           webbrowser.open(f"https://www.google.com/search?q= {ds}") 

       elif 'scroll up' in query:
           speak("please wiat scrolling..")
           pyautogui.scroll(-1000)

       elif 'scroll down' in query:
           speak("please wiat scrolling..")
           pyautogui.scroll(1000)

       elif 'close' in query:
           speak("please wiat closingw..")
           pyautogui.hotkey('alt', 'f4ww')

       elif 'press enter' in query:
           speak("pressing key enter")
           pyautogui.press('enter')

        