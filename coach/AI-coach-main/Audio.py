import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import streamlit as st

def text_to_speech(text):
    audio = False
    tts = gTTS(text=text, lang= 'en')
    if os.path.exists("ai_voice.mp3"):
        os.remove("ai_voice.mp3")
        audio = True
    else:
        audio = True

    if audio:
        filename = 'ai_voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('Exception'+ str(e))

    return said


