import bluetooth
from bluetooth.btcommon import BluetoothError
import time

class NeuroskyConnector:
    target_name = "MindWave Mobile"
    target_address = None
    socket = None


    def getConnectionInstance(self):
        self.deviceDiscovery()
        if(self.target_address is not None):
            print("Device found!")
            self.connect_bluetooth_addr()
            return self.socket
        else:
            print("Could not find target bluetooth device nearby")

    def deviceDiscovery(self):
        try:
            nearby_devices = bluetooth.discover_devices(lookup_names = True, duration=5)
            for bdaddr, name in nearby_devices:
                if bdaddr and name == self.target_name:
                    NeuroskyConnector.target_address = bdaddr
                    NeuroskyConnector.target_name = name
        except BluetoothError, e:
            print "bluetooth is off"

    def connect_bluetooth_addr(addr):
        for i in range(1,5):
            time.sleep(1)
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            try:
                sock.connect((addr.target_address, 1))
                sock.setblocking(False)
                NeuroskyConnector.socket = sock
                return
            except BluetoothError, e:
                print("Could not connect to the device")
        return None