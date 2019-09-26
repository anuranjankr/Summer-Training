import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()
#set threhold level
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))
#r.energy_threshold
# obtain audio from the microphone

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print(r.recognize_google(audio))
'''

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print(r.recognize_google(audio))
'''
