class Tel:

    def __init__(self):
        self.r = open("/mnt/hgfs/share/zuoye/tel.txt", "r")
        self.a = open("/mnt/hgfs/share/zuoye/tel.txt", "a")
        self.lines = self.r.readlines()  #读取文件内容
    def add(self,name,telnum):
        self.a.write(name+'::'+telnum+'\n') #追加信息

    def query(self,name):
        dic= {}
        for i in self.r.readlines():
            info = i.split('::')
            if name == info[0]:
                dic[info[0]] = info[1].strip()
        return dic
        #查询信息

    def dell(self, name):
        self.w = open("/mnt/hgfs/share/zuoye/tel.txt", "w")
        for i in self.lines:
            info = i.split('::')[0]
            if not name == info : #如果name不在文件内就写入一行
                self.w.write(i)
        #删除信息
        self.w.close()
    def modify(self,name,telnum):
        self.w = open("/mnt/hgfs/share/zuoye/tel.txt", "w")
        for i in self.lines:
            info = i.split('::')
            if not name == info[0]:
                self.w.write(i)
            else:
                self.w.write(name+'::'+telnum+'\n')
        
        self.w.close()
    def __del__(self):


        self.r.close()
        self.a.close()

T = Tel()
#T.add('ccc','123123123')
#T.add('asd','sadasda')
#print(T.query('ccc'))
#T.dell('ccc')
T.modify('asd','aaaaaaaaaaaaaaaaa')
