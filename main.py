from gtts import gTTS
import speech_recognition as sr
from googletrans import Translator
import playsound
import os

translator = Translator()


def translator_fun(text):
    return translator.translate(text, src='en', dest='ta')


def text_to_voice(text_data):
    myobj = gTTS(text=text_data, lang='ta', slow=False)
    myobj.save("cache_file.mp3")
    playsound.playsound(sound="C:/Users/muthu/PycharmProjects/pythonProject2/cache_file.mp3")#,player="mpg123")
    os.remove("cache_file.mp3")


while True:
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source, phrase_time_limit=5)
    try:
        print("Processing...")
        spoken_text = rec.recognize_google(audio, language='ta')
        print(spoken_text)
        # print("Translating...")
        # tamil_version = translator_fun(spoken_text)
        # print(tamil_version)
        print("Text to Speech...")
        text_to_voice(spoken_text)#(tamil_version.text)

    except Exception as e:
        print(e)