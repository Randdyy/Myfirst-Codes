import tkinter
import socket
from threading import Thread,Event
import os


class ListenThread(Thread):
    def __init__(self, edit,server):
        Thread.__init__(self)
        self.edit = edit
        self.server = server


    def run(self):
        while True:
            try:
                conn,addr = self.server.accept()
                self.edit.insert(tkinter.END,'接收到来自ip:{}--port{}的连接\n'.format(*addr))
                file1 = open('re.txt','wb')
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file1.write(data)
                self.edit.insert(tkinter.END,'.........\n')
                file1.close()
                self.edit.insert(tkinter.END,'ip{}发来数据：{}\n'.format(addr[0],data))
                conn.sendall('服务器接收到数据'.encode('utf-8'))
                conn.close()
                self.edit.insert(tkinter.end,'关闭客户端')
            except:
                self.edit.insert(tkinter.END,'客户端断开连接')
                break

class ControlThread(Thread):
    def __init__(self, edit):
        Thread.__init__(self)
        self.edit = edit
        self.event = Event()
        self.event.clear()#清空标记
    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('172.25.9.202',5000))
        server.listen(5)
        self.edit.insert(tkinter.END,'现在开始监听\n')
        self.lt = ListenThread(self.edit,server)
        self.lt.setDaemon(True)
        self.lt.start()
        self.event.wait()
        server.close()

    def stop(self):
        self.event.set()

class Window:
    def __init__(self,root):
        self.root = root
        self.btnListen = tkinter.Button(root,
                                        text = '开始监听',
                                        command = self.Listen)
        self.btnListen.place(x = 20,y = 15)
        self.btnClose = tkinter.Button(root,
                                      text = '停止监听',
                                      command = self.Close)
        self.btnClose.place(x = 120,y = 15)
        self.edit = tkinter.Text(root)
        self.edit.place(y = 50)

    def Listen(self):
        '''创建控制线程'''
        self.ctrl = ControlThread(self.edit)
        self.ctrl.setDaemon(True)
        self.ctrl.start()
        
    def Close(self):
        '''结束控制线程'''
        self.ctrl.stop()
    


root = tkinter.Tk()
window = Window(root)
root.mainloop()
