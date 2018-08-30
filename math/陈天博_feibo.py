import time
num = int(input())
l=[1,1]
for i in range(1, num-1):
    x=l[-1]+l[-2]
    l.append(x)
    time.sleep(10)
    print(l)
