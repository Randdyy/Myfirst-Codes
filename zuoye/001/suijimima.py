import string
import random
def password ():
    num = int(input("你想生成几位密码"))
    a=string.printable[0:62]
    for x in range(num):
        i = random.randint(0, 63)
        q=a[i]
        print(q,end='')
    print("\n")
password()
