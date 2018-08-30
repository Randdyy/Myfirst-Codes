l = ["172.16.3.1", "172.16.1.5", "172.15.2.0", "172.16.3.1",
"172.16.3.1","172.16.1.5"]
l1 = []
dic = {}
for i in l:
    if not i in dic:
        dic[i] = 1
    else :
        dic[i] += 1
print(dic)
for k in dic:
    l1.append(dic[k])
p = {value:key for key,value in dic.items()}
print(p)
print("ip{}出现的最多，出现了{}次".format(p[max(l1)]  ,max(l1)))
