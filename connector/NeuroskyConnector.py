import bluetooth
from bluetooth.btcommon import BluetoothError
import time

class NeuroskyConnector:

    """ Class that allows to discover and connect to the mindwave headset thru usb"""

    TARGET_NAME = "MindWave Mobile"
    TARGET_ADDRESS = None
    SOCKET = None

    def __init__(self):
        pass

    def getConnectionInstance(self):
        self.deviceDiscovery()
        if(NeuroskyConnector.TARGET_ADDRESS is not None):
            print("Device found!")
            self.connect_bluetooth_addr()
            return NeuroskyConnector.SOCKET
        else:
            print("Could not find target bluetooth device nearby")
            exit()


    def deviceDiscovery(self):
        try:
            nearby_devices = bluetooth.discover_devices(lookup_names = True, duration=5)
            for bdaddr, name in nearby_devices:
                if bdaddr and name == NeuroskyConnector.TARGET_NAME:
                    NeuroskyConnector.TARGET_ADDRESS = bdaddr
                    NeuroskyConnector.TARGET_NAME = name
        except BluetoothError, e:
            print "bluetooth is off"

    def connect_bluetooth_addr(self):
        for i in range(1,5):
            time.sleep(1)
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            try:
                sock.connect((NeuroskyConnector.TARGET_ADDRESS, 1))
                sock.setblocking(False)
                NeuroskyConnector.SOCKET = sock
                return
            except BluetoothError, e:
                print("Could not connect to the devicee")
        return None