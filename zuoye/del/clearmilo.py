import os
import sys
filetype = ['.tmp','.txt']
def read(l,x):
    m = chuli(l)
    l2 = []
    x = str(x)
    dir1 = m+"/virus"+x+".bak"
    print(dir1)
    with open(l, "r") as r:
        k = r.readlines()
        for i in k:
            i = i.strip()
            i = ''.join(i)
            l2.append(i)
        for j in l2:
            if 'milomilomilo' in j:
                print("renaming...")
                os.rename(l,dir1)

def dell(x):
    l = []
    n = 0
    list1 = os.listdir(x)
    for i in list1:
        a = os.path.join(x, i)
        if os.path.isdir(a):
            dell(a)
        elif os.path.splitext(a)[1] in filetype:
            n = n+1
            read(a,n)

def chuli(l):
    l2 = []
    l3 = l.split('/')
    l3 = l3[0:-1]
    f =  '/'.join(l3)
    return f



if __name__ == '__main__':
    dell("/mnt/hgfs/share")
#dell(sys.argv[1])
