__author__ = 'Administrator'

import socket,os,time

server = socket.socket()

server.bind(("localhost",9999))

server.listen()

while True:
    conn,addr  = server.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break

        cmd,filename = data.decode().split()

        if os.path.isfile(filename)
            f  = open(filename,"rb")
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            print("file_md5",m.hexdigest())
            f.close()
server.close()
