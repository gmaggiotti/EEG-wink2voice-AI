from connector.NeuroskyConnector import NeuroskyConnector
from bluetooth.btcommon import BluetoothError
from neurosky.parser import  ThinkGearParser, TimeSeriesRecorder
import wink, states
from Talk import Talk
import sys
from nnet.A4NN import A4NN

conn = NeuroskyConnector()
socket = conn.getConnectionInstance()
recorder = TimeSeriesRecorder()
parser = ThinkGearParser(recorders= [recorder])


w = wink.Wink()
s = states.States()
t = Talk()
net = A4NN()
net.train()
test_dataset=[87,87,97,97,97,97,97,97,97,97,97,97,107,107,107,107,107,107,167,247,55,29,59,59,29,29,29,129,129,129,129,307,309,92,37,60,72,75,97]
result = net.predict(test_dataset)
print("Output of example should be:" + repr(result))

test_dataset=[85,85,85,85,85,85,85,85,85,72,72,72,97,149,337,436,436,436,436,436,436,436,436,436,436,401,295,55,55,55,55,65,121,141,141,141,141,141,141]
result = net.predict(test_dataset)
print("Output of example should be:" + repr(result))
i=0
myList=[]
while socket is not None:
    try:
        data = socket.recv(1000)
        parser.feed(data)


        max = recorder.raw[-100:].max()

        if(i==39):
            prediction = net.predict(myList)
            print("Output of example should be:" + repr(prediction))
            if( prediction > 0.8 ):
                s.addWink()
            count = s.getWinkWithinDelta()
            if( count == 1 ):
                t.sayYes()
            elif( count == 2 ):
                t.sayNo()
            i=0
            myList = []

        if(i<39):
            myList.append(max)
            i = i + 1


    except BluetoothError:
        pass


