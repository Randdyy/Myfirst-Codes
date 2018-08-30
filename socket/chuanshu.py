
import socket

with socket.socket() as s:

    s.connect(('172.25.10.107',5000))
    file = open('/mnt/hgfs/share/zhengze/images/AR74V590EF7L432X.jpg', 'rb')
    while True:
        sd= file.read(1024)
        if not sd:
            break
        s.send(sd)
    file.close()

