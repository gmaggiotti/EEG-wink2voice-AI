from neurosky.connector.NeuroskyConnector import NeuroskyConnector
from bluetooth.btcommon import BluetoothError


conn = NeuroskyConnector()
socket = conn.getConnectionInstance()

while socket is not None:
    try:
        data = socket.recv(10000)
        print data
    except BluetoothError:
        pass