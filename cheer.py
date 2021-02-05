# using this library (module) called "pyttsx3"
import pyttsx3
# prompt the user to input his name
name = input("What's your name? ")
# init the variable
engine = pyttsx3.init()
# order to say something
engine.say(f"hello, {name}")
# run the order and wait until the end of the voice
engine.runAndWait()
