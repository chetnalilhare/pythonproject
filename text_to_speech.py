import pyttsx3
engine=pyttsx3.init()
while True:
     engine.say(input("write to hear: "))
     engine.runAndWait()
     if engine.say=="q":
      break