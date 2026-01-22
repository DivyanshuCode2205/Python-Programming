import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print(type(voices))
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

engine.say("Hey, its Zira good morning. How can I help you today?")
engine.runAndWait()
