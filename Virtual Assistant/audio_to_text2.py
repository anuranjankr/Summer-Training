#Python 2.x program to transcribe an Audio file 
import speech_recognition as sr
from gtts import gTTS
import os

mytext='Hello This is your program'
print("OK")
myobj=gTTS(text=mytext,lang='en',slow=False)
print("OK")
myobj.save("test_audio.wav")
print("OK")

os.system("test_audio.wav")
print("OK")
#subprocess.call(['ffmpeg', '-i', 'XXX.mp3', 'XXX.wav'])
AUDIO_FILE = ("test_audio.wav")
print("OK")

# use the audio file as the audio source 

r = sr.Recognizer() 
print("yes")
with sr.AudioFile(AUDIO_FILE) as source: 
	#reads the audio file. Here we use record instead of 
	#listen 
	audio = r.record(source)
	print("yes")

try: 
	print("The audio file contains: " + r.recognize_google(audio)) 

except sr.UnknownValueError: 
	print("Google Speech Recognition could not understand audio") 

except sr.RequestError as e: 
	print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
