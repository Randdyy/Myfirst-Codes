def read():
    f = open("/etc/passwd", "r")
    l = f.readlines()
 #   split(l)
    return l


def split(x):
    l = []
    for i in x:
        i = i.strip()
        k = i.split(":")
        l.append(k)
    return l
def pri(l):
    dic={}
    for i in l:
        dic[i[0]]=i[-2],i[-1]
    print(dic)

if __name__ == '__main__':
    pri(split(read()))

