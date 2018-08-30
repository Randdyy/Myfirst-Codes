import threading
import time
import random
def worker(event, name):
    while  not event.is_set():
        print('({}) Waiting to test Mysql connect....'.format(name))
        event.wait(2)
    print('({}) now you can connect to mysql'.format(name))
def counter(event, name, n):
    while True:
        i = random.randint(1,11)
        time.sleep(n)
        if i == 5:
            event.set()
            break




evt_mysql = threading.Event()

t1 = threading.Thread(target=worker, args=(evt_mysql, 't1'))
t1.start()


t2 = threading.Thread(target=worker, args=(evt_mysql, 't2'))
t2.start()

t4 = threading.Thread(target=counter, args=(evt_mysql, 't4', 2))
t4.start()

t3 = threading.Thread(target=counter, args=(evt_mysql, 't3', 5))
t3.start()

#print('first')
#time.sleep(2)
#print('ok')
#evt_mysql.set()

