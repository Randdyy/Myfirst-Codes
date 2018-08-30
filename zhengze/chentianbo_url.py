import urllib.request
import re
import threading
url_python = "http://www.python.org"


def getContent(num):
    url_qsbk="https://www.qiushibaike.com/text/page/{}/".format(num)
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
#    print(m1)
#    print(m2)
#    print(m3)

    for i in range(len(m1)):
        print("用户:"+ m1[i] + " 赞 " + m2[i] + " 内容 " + m3[i])


t1 =  threading.Thread(target=getContent, args=('1',))
t2 =  threading.Thread(target=getContent, args=('2',))
#t3 =  threading.Thread(target=getContent, args=('3',))
#t4 =  threading.Thread(target=getContent, args=('4',))
#t5 =  threading.Thread(target=getContent, args=('5',))
#t6 =  threading.Thread(target=getContent, args=('6',))
#t7 =  threading.Thread(target=getContent, args=('7',))
#t8 =  threading.Thread(target=getContent, args=('8',))
#t9 =  threading.Thread(target=getContent, args=('9',))
#t10 = threading.Thread(target=getContent, args=('10',))


t1.start()
t2.start()
#t3.start()
#t4.start()
#t5.start()
#t6.start()
#t7.start()
#t9.start()
#t8.start()
#t10.start()
