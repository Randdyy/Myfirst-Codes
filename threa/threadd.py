import threading
import time

def func(name,n):
    for i in range(n):
        print(name,i)
        time.sleep(0.3)

t1 = threading.Thread(target=func,args=('t1',5))
t2 = threading.Thread(target=func,args=('t2',100))
t3 = threading.Thread(target=func,args=('t3',15))

t1.start()
t1.join()
print(t3.isAlive())
#t2.daemon = True
t2.start()
print(t2.isDaemon())
print('t2 name:', t2.getName())
print('t2 setname:',t2.setName('ttttt22222'))
print('t2 name:', t2.getName())
t3.start()
print(t3.isAlive())
t3.join()


print('main end')
