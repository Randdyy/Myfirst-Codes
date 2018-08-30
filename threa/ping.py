from threading import Thread
import time
import queue
import subprocess
queue = queue.Queue()

class Producer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self,name=threadname)

    def run(self):
        for i in range(1,255):
            IP = '172.25.2.{}'.format(i)
            queue.put(IP)
#            print(self.getName(),'put', IP, 'to queue')

class Consumer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self, name=threadname)

    def run(self):
        while not queue.empty():
            q = queue.get()
            ret = subprocess.call('ping -c 1 {}'.format(q),shell=True,stdout=open('/dev/NULL','w'),stderr=subprocess.STDOUT)
            if ret == 0:
                print(self.getName(),'get',q,'status:',ret)


            queue.task_done()


clist = []

p = Producer('producer'+str(1))
p.start()
p.join()

for i in range(10):
    c = Consumer('consumer'+str(i))
    clist.append(c)
for i in clist:
    i.setDaemon(True)
    i.start()

queue.join()
