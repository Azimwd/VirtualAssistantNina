from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import speech_recognition as sr
import pyjokes
import webbrowser as wb
from datetime import datetime
from gtts import gTTS
import playsound
import random
import pyowm
import math
import time
import os
from translate import Translator
from fuzzywuzzy import fuzz
import wikipedia
import sys
import json
import datetime
from NinaUI import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from datetime import datetime
 



with open("Base.json","r") as file:
    data = json.load(file)

RNum = random.randint(1, 4)

def say_massage(massage):
    voice = gTTS(massage, lang="ru")
    faile_voice_name = "_audio_" + \
        str(time.time()) + "_" + str(random.randint(0, 100000)) + ".mp3"
    voice.save(faile_voice_name)
    playsound.playsound(faile_voice_name)
    print("голосовой помощник: " + massage)

now = datetime.now()
if (now.hour >= 6 and now.hour < 10):
    say_massage("доброе утро")
elif(now.hour > 12 and now.hour < 18):
    say_massage("добрый день")
else:
    say_massage("добрый вечер")


class MainThread(QThread,QMainWindow):

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        command = self.listen_command()
        self.do_this_command(command)

    def listen_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Дайте команду")
            say_massage("Слушаю вас")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print("Обработка...")
            our_speech = r.recognize_google(audio, language="ru")
            print("Вы сказали:" + our_speech)
            return our_speech
        except sr.UnknownValueError:
            return "ошибка"


    def do_this_command(self, massage):
        massage = massage.lower()

        if "открой браузер" in massage:
            os.system('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Firefox')
            say_massage("принято")
            Nina.stopgif()
            sys.exit()
            
        elif fuzz.partial_ratio("открой whatapp", massage) > 90:
            say_massage("принято")
            os.startfile('C:/Users/User/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/WhatsApp/WhatsApp')
            Nina.stopgif()
            sys.exit()

        elif fuzz.partial_ratio("создать папку", massage) > 90:
            say_massage("как назвать папку?")
            folder = self.listen_command()
            os.mkdir(f"C:/Users/User/Desktop/{folder}")
            Nina.stopgif()

        elif fuzz.partial_ratio("удалить папку", massage) > 90:
            say_massage("какую папку удалить?")
            folder = self.listen_command()
            os.rmdir(f"C:/Users/User/Desktop/{folder}")
            Nina.stopgif()
            
        elif fuzz.partial_ratio("создать документ", massage) > 90:
            say_massage("как назвать документ?")
            file = self.listen_command()
            f = open(f"C:/Users/User/Desktop/{file}.DOCX", "+x")
            Nina.stopgif()

        elif fuzz.partial_ratio("удалить документ", massage) > 90:
            say_massage("какой документ удалить?")
            file = self.listen_command()
            os.remove(f"C:/Users/User/Desktop/{file}.DOCX")
            Nina.stopgif()

        elif fuzz.partial_ratio("найди", massage) > 90:      
            say_massage("скажите запрос")
            brows = self.listen_command()
            wb.open(brows)
            Nina.stopgif()


        elif fuzz.partial_ratio("википедия", massage) > 90:
            say_massage("скажите запрос")
            wiki = self.listen_command()
            total = wikipedia.summary(wiki, sentences=3)
            say_massage(total)
            Nina.stopgif()

        elif fuzz.partial_ratio("переведи", massage) > 90:
            # say_massage("скажите язык на который нужно перевести c ангиского")

            # language = self.listen_command()
            # language = 'russian'
            say_massage("скажите слово которое нужно перевести")
            word = self.listen_command()

            translator = Translator(to_lang='russian')
            translation = translator.translate(word)
            say_massage(translation)
            Nina.stopgif()

        elif fuzz.partial_ratio("какая сейчас погода", massage) > 90:
            say_massage("Погоду какого города вы хотите узнать?")
            cyty = self.listen_command()
            owm = pyowm.OWM("519d080cce3b76306db4b7bc31fdd533")
            mgr = owm.weather_manager()

            observation = mgr.weather_at_place(cyty)
            w = observation.weather
            weather = w.detailed_status
            temp = w.temperature('celsius')

            language = "Russian"
            word = weather
            translator = Translator(to_lang=language)
            translation = translator.translate(word)
            say_massage(translation)
            say_massage("сейчас " + str(math.ceil(temp["temp"])) + " градусов")
            Nina.stopgif()

        elif fuzz.partial_ratio("расскажи шутку", massage) > 90:
            language = "Russian"
            word = pyjokes.get_joke()
            translator = Translator(to_lang=language)
            translation = translator.translate(word)
            say_massage(translation)
            Nina.stopgif()

        elif fuzz.partial_ratio("привет", massage) > 90:
            say_massage(data["hello"][0][str(RNum)])
            Nina.stopgif()

        elif fuzz.partial_ratio("сколько время", massage) > 90:
            say_massage(datetime.now().strftime('%H часов %M минут'))
            Nina.stopgif()

        elif fuzz.partial_ratio("Скажи точное время", massage) > 90:
            say_massage(datetime.now().strftime('%H часов %M минут %S секунд'))
            Nina.stopgif()

        elif fuzz.partial_ratio("спасибо", massage) > 90:
            say_massage(data["thank"][0][str(RNum)])
            Nina.stopgif()

        elif fuzz.partial_ratio("как дела", massage) > 90:
            say_massage(data["how are you"][0][str(RNum)])
            Nina.stopgif()

        elif fuzz.partial_ratio("сменить имя", massage) > 90:
            say_massage("Как вы хотите меня назвать ")
            self.data["Name"] = self.listen_command()
            with open('Base.json', 'w') as f:
                json.dump(data, f, indent=2)
            say_massage("имя изменено на " + data["Name"])
            Nina.stopgif()

        elif fuzz.partial_ratio("как тебя зовут", massage) > 90:
            say_massage(data["Name"])
            Nina.stopgif()

        elif fuzz.partial_ratio("пока", massage) > 90:
            say_massage("Пока")
            Nina.stopgif()
            sys.exit()
            
        else:
            print('отключаюсь')
            Nina.stopgif()


execution = MainThread()


class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.Say.clicked.connect(self.Voice_helper_start)
        self.ui.Say.clicked.connect(self.startgif)
 

    def startgif(self):
        self.ui.movie = QtGui.QMovie("img/LCPT.gif")
        self.ui.circle2.setMovie(self.ui.movie)
        self.ui.movie.start()  


    def stopgif(self):
        self.ui.movie = QtGui.QMovie("img/LCPT.gif")
        self.ui.circle2.setMovie(self.ui.movie) 
        self.ui.movie.stop()
            

    def Voice_helper_start(self):
        execution.start()



app = QApplication(sys.argv)
Nina = Mywindow()
Nina.show()
exit(app.exec_())