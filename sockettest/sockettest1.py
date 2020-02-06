# socket 套接字
# Python中提供socket.py标准库，非常底层的接口库
# Socket是一种通用的多几张编程掊，和网络层次没有，对应的关系
# 协义族
# AF表示Address Family ，用于socket()第一个参数
# AF_INET IPV4
# AF_INET IPV6
# AF_UNIX   unix domain Socket ,window 没有
# 提供一个相对而言稳定的通道，都不关心你在不在，
# 上列accep和recv是阻塞的，主线程经常被阻塞住而不能工作，怎么办
#
from socket import socket

server = socket()
server.bind('127.0.0.1', 9999)
server.listen()
s, raddr = server.accept()

while True:
    data = s.recv(1024)
    print(data)
    s.send('ack.{}'.format(data.decode()).encode())

s.close()
server.close()
