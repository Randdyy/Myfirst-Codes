import threading
import time
class MyTread(threading.Thread):
    def __iniit__(self, name ):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(10):
            print('this is {} {}'.format(i,self.name))
            time.sleep(0.5)
t1 = MyThread('T1')
t2 = MyThread('T2')
t3 = MyThread('T3')




t1.start()
t2.start()
t3.start()
