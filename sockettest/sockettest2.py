# 写一个群聊程序
# 需求分析
# 聊天工具是cs的程序，c是每一个客户端，s是服务器端
# 服务器应该具有功能：
#   启动服务器，包括绑定地址和商品，监听
#   建立连接，能和多个客户端建立连接
#   接收不同的用户信息
#   分发，将接收某个用户的信息转发到已经连接的所有客户端
#   socket.recv(bufsize[,flags]) 获取数据，默认的阻塞方式
#   socket.recvfrom(bufsize[,flags]) 获取数据，返回一个二元组（bytes,address）
#   socket.recv_into(buffer[,nbytes[,flags]])
#   socket.send(bytes[,flags]) TCP数据
#   socket.sendall(bytes[,flags])   TCP发送全部数据，成功返回None
#   s.sendto(string[,flag],address)     UDP发送数据
#   socket.sendfile(file,offset=0,count=None) 发送一个文件直到EOF,使用高性能的os.sendfile机制，返回发送字节数，
#   如果 win下不支持sendfile，或者不是普通文件，使用send()发送文件，offset告诉起始位置，3.5版本开始
#   socket.makefile(mode='r',buffer)
#   socket.getsockname()        返回套接字自己的地址，通常走一个元组（ipaddr,port）
#   socket.setblocking(flag)    如果flag为0,则将套接字设置为非阻塞模式，默认值,非阻塞模式下
#   socket.settimeout(value)    这是一个
#


import datetime
from socket import socket
import threading
import logging

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatServer:
    def __init__(self, ip, port):
        self.addr = (ip, port)
        self.socket = socket()
        self.clents = {}
        self.event = threading.Event()

    def start(self):
        self.socket.bind(self.addr)
        self.socket.listen()  # 服务启动
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set():
            s, addr = self.socket.accept()  # 阻塞
            #s.makefile(mode='rw')
            logging.info(s)
            logging.info(addr)
            self.clents[addr] = s
            threading.Thread(target=self.recv, name='recv', args=(s,)).start()

    def recv(self, socket: socket):
        while not self.event.is_set():
            try:
                data = socket.recv(1024)  # 阻塞，bytes
                logging.info(data)
            except Exception as e:
                logging.error(e)
                data == b'quit'

            if data == b'quit':
                self.clents.pop(socket.getpeername())
                socket.close()
                break

            msg = "ack {} {}".format(
                socket.getpeername(),
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                data.decode()).encode()

            for s in self.clents.values():
                s.send(msg)

    def stop(self):
        for s in self.clents.values():
            s.close()
        self.socket.close()
        self.event.set()


cs = ChatServer()
cs.start()

while True:
    cmd = input(">>>>")
    if cmd.strip() == 'quit':
        cs.stop()
        threading.Event.wait(3)
        break
    logging.info(threading.enumerate())
