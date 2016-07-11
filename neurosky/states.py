import time

class States:

    def __init__(self):
        self.t1 = 0
        self.winks = 0

    def addWink(self):
        self.winks += 1
        if( self.t1 == 0 ):
            self.t1 = time.time()


    def getWinkWithinDelta(self):
        w = self.winks
        delta = time.time() - self.t1
        print delta
        print w

        if(delta > 2 ):
            self.t1 = 0
            self.winks = 0
            return w
        return 0

