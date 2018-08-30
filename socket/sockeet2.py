import socket
import time
import threading

def Sending(ss,address):
    while True:
        user_input = input("I say")
        if user_input!='q':
            ss.sendto(user_input.encode('utf-8'),(address,60008))
      

def Reading(sss):
    while True:
        data,addr = sss.recvfrom(1024)
        print(sss.recvfrom)
        print("{}says{}".format(addr[0], data.decode('utf-8')))
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    HOST = '172.25.9.202'
    PORT = 55355
    s.bind((HOST,PORT))
    ipaddr = str(input('输入对方的ip'))
    T1 = threading.Thread(target=Sending,args=(s,ipaddr))
    T2 = threading.Thread(target=Reading,args=(s,))
    T1.setDaemon(True)
    T2.setDaemon(True)
    T1.start()
    T2.start()
    T1.join()
    T2.join()
