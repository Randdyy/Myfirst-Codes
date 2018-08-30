import socket

HOST = '172.25.9.202'
PORT = 55555
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(str(data).split("'")[1])
            if not data:break
            conn.sendall(b'asdsad'+data)
