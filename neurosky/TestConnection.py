from neurosky.connector.NeuroskyConnector import NeuroskyConnector
from bluetooth.btcommon import BluetoothError
from parser import  ThinkGearParser, TimeSeriesRecorder
import pyttsx
import time


conn = NeuroskyConnector()
socket = conn.getConnectionInstance()
recorder = TimeSeriesRecorder()
parser = ThinkGearParser(recorders= [recorder])


blink_start = 0

while socket is not None:
    try:
        data = socket.recv(10000)
        parser.feed(data)
        median = recorder.raw[-1000:].median()

        if( median > 41 and blink_start == 0):
            blink_start = 1
        if( median < 39 and blink_start != 0 ):
            blink_start=0;
            print("####################  1 blink")
            engine = pyttsx.init()
            engine.setProperty('rate', 60)
            engine.say("Yes")
            time.sleep(1)
            engine.runAndWait()
            time.sleep(1)

        #print("Median:" + str(median))

    except BluetoothError:
        pass


