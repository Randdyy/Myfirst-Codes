import os
import sys
filetypes = ['.tmp']
l2=[]
def del1(x):
    list1 = os.listdir(x)
    for i in list1:
        a = os.path.join(x,i)
        if os.path.isdir(a):
            del1(a)
        elif os.path.splitext(a)[1] in filetypes:
            os.chmod(a,777 )
            os.remove(a)
            print(a, 'deleted....')


if __name__ == '__main__':
    paths = sys.argv[1:]
    for path in paths:
        if os.path.isdir(path):
            del1(path)
