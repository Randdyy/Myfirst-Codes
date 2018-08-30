import urllib.request
import re
from threading import Thread,Condition
import time
class Producer(Thread):
    def __init__(self,num):
        Thread.__init__(self)
        self.num = num
#		self.run(self.num)
    def run(self):
        url_qsbk="https://www.qiushibaike.com/text/page/{}/".format(self.num)
        user_agent = "Chrome/4.0(compatible; MSIE 5.5;Windows NT"
        req = urllib.request.Request(url_qsbk, headers={"User-Agent":user_agent})
        page = urllib.request.urlopen(req)
        html = page.read().decode('utf-8')

        html = html.replace("<br/>","")
        r1 = r'<h2>\s*?(.*?)\s*?</h2>'
        r2 = r'<span class="stats-vote"><i class="number">(.*?)</i>'
        r3 = r'<div class="content">\s*<span>\s*(.*?)\s*</span>'
        m1 = re.findall(r1,html,re.S)
        m2 = re.findall(r2,html,re.S)
        m3 = re.findall(r3,html,re.S)
#print(m1)
#print(m2)
#print(m3)

        for i in range(len(m1)):
            print("用户:"+ m1[i] + " 赞 " + m2[i] + " 内容 " + m3[i])



l = []
for i in range(1,10):
    p = Producer(str(i))
    l.append(p)

for i in l:
    i.start()
