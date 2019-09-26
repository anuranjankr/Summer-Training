import speech_recognition as sr
from time import ctime
import time
import os
import vlc
import webbrowser
import pafy
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    #os.system("mpg321 audio.mp3")
    player = vlc.MediaPlayer("audio.mp3")
    player.play()
    time.sleep(1)

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
        if "what time is it" in data:
            speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Anuranjan, I will show you where " + location + " is.")
        #os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
    if "play" in data:
        data=data.split(" ")
        song = data[1:]
        url="https://www.youtube.com/results?search_query="
        for word in song:
            url+= word + "+"
        url=url[:-1]
        #webbrowser.open_new(url)
        import urllib.request
        import urllib.parse
        import re

        #query_string = urllib.parse.urlencode({"search_query" : input()})
        print("1")
        html_content = urllib.request.urlopen(url)
        print("2")
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        print("3")
        video_url="http://www.youtube.com/watch?v=" + search_results[0]
        webbrowser.open_new(video_url)
    if "tell me about" in data:
        data=data.split(" ")
        import wikipedia
        about=wikipedia.page(data[3:])
        webbrowser.open_new(about.url)
        
# initialization

speak("Hi Anuranjan, what can I do for you?")
time.sleep(2)
while 1:
    data = recordAudio()
    jarvis(data)
