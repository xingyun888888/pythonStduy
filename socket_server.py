__author__ = 'Administrator'

import socket


#服务端

server  = socket.socket()

#绑定要监听的端口
server.bind(("localhost",6969))

#监听
server.listen()
#等待发送数据
conn,addr = server.accept()

print("电话来了")
while True:
    data = conn.recv(1024)

    print("recv:",data.decode("utf-8"))

    #返回给客户端一个值
    conn.send(data.upper())

server.close()
'''
 server.accept()默认是阻塞的
 客户端已断开 while里面就死循环了 conn.recv()收到的是空数据
 为了避免死循环 需要判断
 if not data:
   break #客户端断开

 怎么让它在回过去 再加一个循环
  然后又回到这里 不断的接收新连接
  同时同时只能服务一个新连接

客户端 第一步 实例化一个socket client = socket.socket()

client.connect(("localhost",port))

client.send()

client.recv(1024)



#服务端
import socket

server = socket.socket()
server.bind("localhost",9999)

server.listen()

while True:
  conn,addr = server.accept()
  print("new conn":,addr)
  while True:
    data = conn.recv(1024)
    if not data
      print("客户端已经断开...")
      break
    print("执行指令:",data)

'''

