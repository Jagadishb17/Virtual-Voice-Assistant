import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from Youtube import *
from Maps import *
from News import *
import randfacts
from jokes import *
import datetime
import Generative as hg


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',140)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello , i'm your voice assistant.")

#with sr.Microphone() as source:
#    r.energy_threshold=10000
#    r.adjust_for_ambient_noise(source,1.2)
#    print("listening..")
#    audio = r.listen(source)
#    text = r.recognize_google(audio)
#    print(text)

#if "what" in text and "about" in text and "you" in text:
#    speak("I am also having good day sir")
speak("What can i do for you ?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)

if "information" in text2:
    speak("you need information related to which topic ?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        print(infor)
    speak("searching in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play"in text2 and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)

    print("playing {} on youtube".format(vid))
    speak("playing video in youtube")

    assist = music()
    assist.play(vid)

elif "date" in text2 or "time" in text2:
    today_date = datetime.datetime.now()
    print("Today is " + today_date.strftime("%d") + " of" + today_date.strftime("%B") + " and its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
    speak("Today is "+today_date.strftime("%d") + "of" + today_date.strftime("%B") + "and its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))


elif "news" in text2:
    arr = news()

    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
        if i==2:
            break


elif "joke" in text2 or "jokes" in text2:
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])


elif "fact" in text2 or "facts" in text2:
    r=randfacts.get_fact()
    print(r)
    speak("Do you know that "+r)


elif "maps" in text2 or "directions" in text2:
    speak("Which location do you like to show me ?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        loc = r.recognize_google(audio)
    speak("opening Google maps")

    assist = maps()
    assist.place(loc)
    assist.direction()

    speak("please tell me your starting location")
    with sr.Microphone() as sour:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(sour,1.2)
        print("listening...")
        aud = r.listen(sour)
        loca = r.recognize_google(aud)
    speak("Directing to your location")
    assist.start_point(loca)


else:
    r=hg.GenAi(text2)
    print(r.text)
    speak(r.text)
