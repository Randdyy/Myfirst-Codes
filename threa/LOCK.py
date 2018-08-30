from threading import Thread,RLock
import time
class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    def run(self):
        global x
        lock.acquire()
        for i in range(3):
            x+=1
        time.sleep(1)
        print('x={}'.format(x))
#        lock.release()
lock = RLock()

tl= []
for i in range(10):
    t = MyThread(str(i))
    tl.append(t)

x = 0
for i in tl:
    i.start()
