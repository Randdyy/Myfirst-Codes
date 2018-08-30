from ftplib import FTP
import sys
class Ftpp():
    def __init__(self,local='172.25.2.203'):
        self.ftp = FTP(local)
        self.ftp.connect(local)
        self.ftp.login()

    def LSS(self):
        self.ftp.retrlines('LIST')

    def PUT(self,path):
        put_path = 'STOR ' + path
        self.ftp.storbinary(put_path, open(path,'rb'))


    def CWD(self,target):

        self.ftp.cwd(target)



a = Ftpp()
a.LSS()
a.CWD('08-url-socket')
print('\n')
a.LSS()
#a.PUT('chentianbo_images.py')
#flag = True
'''while flag:
    user_input = input()
    if user_input == 'ls':
        a.LSS()
    if user_input == 'cd':
        a.CWD('07-RE')
    if user_input == 'q':
        flag = False
    if user_input == 'put':
        a.PUT('/mnt/hgfs/share/zhengze/httpd.py')'''

