import urllib.request
import re
num = 0
url_python = "http://www.python.org"
for i in range(1):
    num=1
    url_qsbk="https://www.qiushibaike.com/pic/page/{}/?s=5115861".format(num)
    user_agent = "Chrome/4.0(compatible; MSIE 5.5;Windows NT"
    req = urllib.request.Request(url_qsbk, headers={"User-Agent":user_agent})
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    r = r'''<div class="thumb".*?<img src="(.*?\.jpg)'''
    m = re.findall(r,html,re.S)
    for j in m:
        l = j.split('/')[-1]
        urllib.request.urlretrieve('http:'+j,'/mnt/hgfs/share/zhengze/images/'+l)
