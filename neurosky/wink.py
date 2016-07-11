from Talk import Talk

class Wink:

    talk = Talk()

    def __init__(self):
        self.blink_start = 0
        self.t1 = 0
        self.t2 =0

    def detectWink(self, max):
        if( max > 400 and self.blink_start == 0):
            self.blink_start = 1
        if( max < 400 and self.blink_start != 0 ):
            self.blink_start=0;
            return 1
        #     if(self.t1 == 0 and self.t2 == 0 ):
        #         self.t1 = time.time()
        #     elif(self.t2 == 0):
        #         self.t2 = time.time()
        #         delta = self.t2 - self.t1
        #         if( delta > 5 ):
        #             print "yes"
        #             self.t1 = self.t2
        #             self.t2 = 0
        #             self.talk.sayYes()
        #         else:
        #             print "no"
        #             self.t1 = self.t2 = 0
        #             self.talk.sayNo()
        #
        # if(self.t1 > 0 and self.t2 == 0 and time.time() - self.t1 > 5 ):
        #     print "yes"
        #     self.talk.sayYes()
        #     self.t1 = self.t2 = 0
        #     self.talk.sayYes()
 #       print max
            # time.sleep(1)
            # engine.runAndWait()
            # time.sleep(1)