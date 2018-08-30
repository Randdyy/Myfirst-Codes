import os
import subprocess
import threading
import queue
q = queue.Queue()
class BackUp():
    def __init__(self,path_s,path_d):#指定路径和目标路径
        self.path_d = path_d
        for file_name in os.listdir(path_s):
            self.file_path = os.path.join(path_s, file_name)#拼接文件路径
            self.newfile_path = os.path.join(path_d, file_name)
            pass#创建新目录
        self.path_size = os.path.getsize(self.file_path)#获取文件大小
        self.f = open(self.file_path,'r+')#读取文件内容

        self.w = open(self.path_d,'a')
    def run(self):
        if self.path_size > 500 and not os.path.isdir(self.file_path):#文件大小符合要求
            self.times =  int(self.path_size/500)+1
                for i in range(self.times+1):
                    self.content = self.f.read(500)
                    q.put(self.content)#放入队列

    def Backup(self):
        content2 = q.get()
        ret = subprocess.call('cp {} {}'.format(self.file_path,
            self.path_d),shell=True,
            stdout=open('/dev/null','w'),
            stderr=subprocess.STDOUT)







