from threading import Thread,Condition
import time
class Producer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self, name=threadname)

    def run(self):
        global x
#        con.acquire()
        if x == 100000000:
            con.wait()
            pass
        else:
            for i in range(100000000):
                x+=1
#       con.notify()
        print(x,'p')
#        con.release()

class Consumer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self, name=threadname)

    def run(self):
        global x
#        con.acquire()
        if x == 0:
#            con.wait()
            pass
        else:
            for i in range(100000000):
                x-=1
#        con.notify()
        print(x,'c')

con = Condition()
x = 0
p = Producer('pro')
c = Consumer('con')
p.start()
c.start()
p.join()
c.join()
print(x)
