import datetime
from socket import socket
import threading
import logging
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

#注意，UDP是无连接协义的，所以可以只有任意一端，例如客户端数据发往服务端，服务端存在卖不无所谓
# UDP编程bind,connect,send,recv,recvfrom 方法使用
# send方法，需要和connect配合使用，可以使用已经从本地商品把数据发往raddr指定端口
# recv方法，需求一定要在占用了本地商品，返回接收数据
#

class ChatUdpServer:
    def __init__(self,ip='0.0.0.0',port=9999):
        self.addr = (ip,port)
        self.socket=socket()
        self.event = threading.Event()

    def start(self):
        self.socket.bind(self.addr) # 启动绑定本地地址和端口udp
        threading.Thread(target=self.recv,name = 'recv').start()

    def recv(self):
        while not self.event.is_set():
            data ,raddr = self.socket.recvfrom(1024)
            logging.info(data)
            logging.info(raddr)
            msg = 'Ack {} .from :{}'.format(data,*raddr).encode()
            self.socket.sendto(msg,raddr)

    def stop(self):
        self.socket.close()
        self.event.set()


if __name__ == '__main__':
    cs = ChatUdpServer()
    cs.start()
    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            break
    cs.send(cmd)
    print(threading.enumerate())


