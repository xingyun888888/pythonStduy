__author__ = 'Administrator'

import socket

client = socket.socket()

client.connect(("localhost",9999))

while True:
    cmd = input(">>").strip()
    if len(cmd)== 0:continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server_response",server_response)
        client.send(b"ready to recv file")
        file_total_size = int(server_response.decode())
        receive_size = 0
        filename = cmd.split()[1]
        f = open(filename,"wb")
        while response_size<file_total_size:
           data = client.recv(1024)
           receive_size +=len(data)
           print(file_total_size,receive_size)
           f.write(data)
        else:
            print("file receive done")