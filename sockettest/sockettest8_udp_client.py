import datetime
import socket
import threading
import logging

# 上面的例子中，如果客户端断开了，服务端知道了，每一个服务端还需要对所有的客户端发送的数据，包括已经断开的客户端
# 代码改进
# 加一个ack机制和心跳heartbeat，心跳，就是一端定时发往另一端的信息，一般每次数据越少越好，心跳时间间隔写好就好了
# ack即响应，一端收到另一端的消息后返回的信息
#

FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

# client = socket.socket(type=socket.SOCK_DGRAM)
# raddr = ('127.0.0.1', 9999)
# client.connect(raddr)
# client.sendto(b'hello', raddr)
# data, addr = client.recvfrom(1024)
# logging.info(data)
# client.close()


class ChatUdpClient:
    def __init__(self,rip,rport=9999,interval=10):
        self.raddr = (rip,rport)
        self.socket = socket.socket(type,socket.SOCK_DGRAM)
        self.event = threading.Event()
        self.interval = interval


    def start(self):
        self.socket.connect(self.raddr)
        threading.Thread(target=self.hb,name='heartbeat').start()
        threading.Thread(target=self.recv,name='recv').start()

    def hb(self):
        while not self.event.wait(self.interval):
            self.send('^hb^')


    def recv(self):
        while not self.event.is_set():
            data,addr = self.socket.recvfrom(1024)
            logging.info(data)
            logging.info(addr)

    def send(self,msg:str):
        self.socket.sendto("{}\n".format(msg).encode())

    def stop(self):
        self.socket.close()

def main():
    cc = ChatUdpClient(interval=5)
    cc.start()
    while True:
        cmd  = input('Plz input you msg:')
        if cmd.strip() == 'quit':
            cc.stop()
            break
        logging.info(threading.enumerate())
        cc.send(cmd)

if __name__ == '__main__':
    main()