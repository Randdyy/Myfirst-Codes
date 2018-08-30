import socket

def checkPort(address, port):
    s = socket.socket()
    try:
        s.connect((address, port))
        print('connect!!!')
        return True
    except socket.error:
        print("connection to %s on port %s failed" %(address,port))

        return False

for i in range(1025):
    checkPort('192.168.171.129',int(i))
