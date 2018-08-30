from threading import Thread
import time 
import queue
queue = queue.Queue()


class Producer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self,name = threadname)

    def run(self):
        global queue
        queue.put(self.getName())
        print(self.getName(), 'put', self.getName(), 'to queue')

class Consumer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self, name = threadname)

    def run(self):
        global queue
        print(self.getName(), 'get', queue.get(), 'form queue')

plist = []
clist = []

for i in range(10):
    p = Producer('producer'+str(i))
    plist.append(p)

for i in range(10):
    c = Consumer('Consumer'+str(i))
    clist.append(c)

for i in plist:
    i.start()
    i.join()

for i in clist:
    i.start()
    i.join()
