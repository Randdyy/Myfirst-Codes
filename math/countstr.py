def countstr():
    x = str(input("please in put a string"))
    l = list(x)
    dic = {}
    for i in l:
        if not i in dic.keys():
            dic[i] = 1
            continue
        elif i in dic.keys():
            dic[i] = dic[i]+1
    for k in dic:
        print("字符{}一共出现了{}次".format(k,dic[k]))
            

countstr()





