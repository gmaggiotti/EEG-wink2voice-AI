from neurosky.connector.NeuroskyConnector import NeuroskyConnector
from bluetooth.btcommon import BluetoothError
from parser import  ThinkGearParser, TimeSeriesRecorder
import pyttsx
import time
import wink


conn = NeuroskyConnector()
socket = conn.getConnectionInstance()
recorder = TimeSeriesRecorder()
parser = ThinkGearParser(recorders= [recorder])

engine = pyttsx.init()
engine.setProperty('rate', 60)
engine.say("Yes")

w = wink.Wink()

while socket is not None:
    try:
        data = socket.recv(1000)
        parser.feed(data)


        max = recorder.raw[-500:].max()
        w.hasWinked(max)

      #  print("max:" + str(max))

    except BluetoothError:
        pass


