l = []
def sum35():
    sum1 = 0
    a = int(input("第一个数"))
    b = int(input("第二个数"))
    s = 0
    for i in range(b):
        s = s+1
        l.append('1'*s)
    for j in l:
        x = int(j)
        sum1 =x*a+sum1
    print(sum1)
    return sum1
sum35()





