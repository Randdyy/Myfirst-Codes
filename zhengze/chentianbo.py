import re

r2 = r'''(?P<IP>\S+)\s.*?".*?" (?P<status>\d+) (?P<Size>\d+|-)'''

with open('/etc/httpd/logs/access_log','r') as r:
    lines = r.readlines()
#print(lines)
dic2 = {}
for i in lines:
    i.strip()
    m=re.match(r2,i)
    dic = m.groupdict()
    if dic['IP'] not in dic2.keys():
        dic2[dic['IP']] = [dic['status']]
    else:
        dic2[dic['IP']].append(dic['status'])
    
print(dic2)



#print(lines[0])
#m=re.match(r2,lines[0])
#print(m)
#print(m.groupdict())

