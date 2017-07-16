import numpy as np
import os

def sigmoid(x, deriv=False):
    if(deriv == True):
        return x*(1-x)
    return 1/(1 + np.exp(-x))

path = os.path.dirname(os.path.abspath(__file__))

class A4NN:

    def __init__(self):

        self.X = 2*np.loadtxt(path+"/train_dataset.csv",delimiter=",")/600 - 1
        self.y = np.loadtxt(path+"/label_dataset.csv",delimiter=",").reshape(self.X.__len__(),1)
        self.syn0 = 2*np.random.random((self.X.size/self.X.__len__(),self.X.__len__())) - 1
        self.syn1 = 2*np.random.random((self.X.__len__(),self.X.__len__())) - 1
        self.syn2 = 2*np.random.random((self.X.__len__(),1)) - 1


    def train(self):
        # X = 2*np.loadtxt(path+"/train_dataset.csv",delimiter=",")/600 - 1
        # y = np.loadtxt(path+"/label_dataset.csv",delimiter=",").reshape(X.__len__(),1)

        # np.random.seed(1)
        # syn0 = 2*np.random.random((X.size/X.__len__(),X.__len__())) - 1
        # syn1 = 2*np.random.random((X.__len__(),X.__len__())) - 1
        # syn2 = 2*np.random.random((X.__len__(),1)) - 1

        for j in xrange(60000):

            # Calculate forward through the network.
            l0 = self.X
            l1 = sigmoid(np.dot(l0, self.syn0))
            l2 = sigmoid(np.dot(l1, self.syn1))
            l3 = sigmoid(np.dot(l2, self.syn2))

            # Error back propagation of errors using the chain rule.
            l3_error = self.y - l3
            if(j % 10000) == 0:   # Only print the error every 10000 steps, to save time and limit the amount of output.
                print("Error: " + str(np.mean(np.abs(l3_error))))

            l3_adjustment = l3_error*sigmoid(l3, deriv=True)
            l2_error = l3_adjustment.dot(self.syn2.T)

            l2_adjustment = l2_error*sigmoid(l2, deriv=True)
            l1_error = l2_adjustment.dot(self.syn1.T)

            l1_adjustment = l1_error*sigmoid(l1,deriv=True)

            #update weights for all the synapses (no learning rate term)
            self.syn2 += l2.T.dot(l3_adjustment)
            self.syn1 += l1.T.dot(l2_adjustment)
            self.syn0 += l0.T.dot(l1_adjustment)

        print("Output after training")
        print(l3)

    def predict(self,X1):
        l0 = np.zeros((self.X.__len__(),self.X.size/self.X.__len__()))
        l0[0] = 2*np.asanyarray(X1, dtype=np.float32)/600 - 1
        l1 = sigmoid(np.dot(l0, self.syn0))
        l2 = sigmoid(np.dot(l1, self.syn1))
        l3 = sigmoid(np.dot(l2, self.syn2))
        return l3[0] #since process X1[0] output would be l2[0]


