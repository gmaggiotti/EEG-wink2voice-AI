import pyttsx
import time

class Talk:

    def __init__(self):
        self.engine = pyttsx.init()
        self.engine.setProperty('rate', 70)

    def sayYes(self):
        self.engine.say("Yes")
        time.sleep(1)
        self.engine.runAndWait()

    def sayNo(self):
        self.engine.say("No")
        time.sleep(1)
        self.engine.runAndWait()

    def sayHelp(self):
        self.engine.say("Help")
        time.sleep(1)
        self.engine.runAndWait()

