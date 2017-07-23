from connector.NeuroskyConnector import NeuroskyConnector
from bluetooth.btcommon import BluetoothError
from neurosky.parser import  ThinkGearParser, TimeSeriesRecorder
import sys

conn = NeuroskyConnector()
socket = conn.getConnectionInstance()
recorder = TimeSeriesRecorder()
parser = ThinkGearParser(recorders= [recorder])




while socket is not None:
    try:
        data = socket.recv(1000)
        parser.feed(data)

        max = recorder.raw[-100:].max()
        sys.stdout.write(str(max)+',')

    except BluetoothError:
        pass


