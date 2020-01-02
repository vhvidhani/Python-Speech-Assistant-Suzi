import speech_recognition as sr 
import playsound 
from gtts import gTTS 
import random
from time import ctime
import webbrowser
import ssl
import certifi
import time
import os 

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source: 
        if ask:
            speak(ask)
        audio = r.listen(source)  
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  
        except sr.UnknownValueError: 
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') 
        print(f">> {voice_data.lower()}") 
        return voice_data.lower()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) 
    playsound.playsound(audio_file) 
    print(f"Emily: {audio_string}") 
    os.remove(audio_file) 

def respond(voice_data):
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is Suzi")
        else:
            speak("my name is Suzi. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)

    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[4].split(":")[0:2]
        print(time)
        hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    if there_exists(["find location"]):
        search_term = voice_data.split("location ")[-1]
        url = f"https://google.nl/maps/place/{search_term}/&amp"
        webbrowser.get().open(url)
        speak(f'Here is what I found for location {search_term} on google maps')


    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    if there_exists(["exit", "quit", "goodbye", "good bye"]):
        speak("going offline")
        exit()


time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio() 
    respond(voice_data) 