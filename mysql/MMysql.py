import pymysql
class MySql():

    def __init__(self,dbname):
        self.conn=pymysql.connect(host='localhost',user='root',password='',db=dbname)
        #self.tbname=tbname
        self.cur = self.conn.cursor()#生成###游标###
        print("成功连接mysql....")


    def Flush(self):
        self.sql_num = self.cur.execute("select * from new")
        self.conn.commit()


    def insert(self,ID,password):
        '''第一个参数为用户id
           第二个为用户名密码
        '''
        self.cur.execute("insert into new value (%s,%s)",(ID,password))
        self.Flush()

    def Query(self):
        self.Flush()
        print(self.cur.fetchmany(self.sql_num))


    def Remove(self,ID):
        '''需要一个ID参数，然后删除'''
        self.cur.execute("delete from new where ID=%s",(ID))
        self.Flush()

    def UpdatePwd(self,password,ID):
        '''通过查找ID 更改密码'''
        self.cur.execute("update new set password=%s where ID=%s",(password,ID))
        self.Flush()

    def UpdateID(self,ID,password):
        '''通过查找ID 更改ID'''
        self.cur.execute("update new set ID=%s where password=%s",(ID,password))
        self.Flush()

    def Roll(self):
        self.Flush()
        a = self.sql_num
        a = -a
        self.cur.scroll(a)#回滚


    def __del__(self):
        self.conn.close()
        self.cur.close()



if __name__=="__main__":
    ms = MySql('test','new')
    ms.insert('qqqq','7777')
    #ms.Remove('pxxx')
    #ms.UpdatePwd('8888','qqqq')
    ms.Query()

