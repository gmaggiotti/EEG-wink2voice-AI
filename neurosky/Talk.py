import pyttsx
import time
engine = pyttsx.init()
engine.setProperty('rate', 70)

while 1:
    engine.say("Yes")
    time.sleep(1)
    engine.runAndWait()