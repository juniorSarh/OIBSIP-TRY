from ast import Try
from dis import Instruction
from logging.config import listen
from multiprocessing.connection import Listener
from platform import machine
import speech_recognition as aa
import pyttsx3

Listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)

machine.runAndWait()

def input_Instruction():

    try: 
        with aa.Microphone() as origin:
            print("listening")
            speech = Listener.listen(origin)
            intruction = Listener.recognize_google(speech)
            Instruction = Instruction.lower()
            if 'voice' in Instruction:
                print(Instruction)
            print(Instruction)


    except:

       pass
