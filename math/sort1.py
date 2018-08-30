l=[]
for p in range(10):
    print("请输入十个字符")
    str1=input()
    l.append(str1)
print(l)
flag=True
while flag:
    flag = False
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
            flag = True
    print(l)
