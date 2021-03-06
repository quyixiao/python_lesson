import datetime
from socket import socket
import threading
import logging

#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
# 我们经常使用心跳机制，先有一个基本的

class ChatUdpServer:
    def __init__(self, ip='0.0.0.0', port=9999):
        self.addr = (ip, port)
        self.socket = socket()
        self.event = threading.Event()
        self.clients = set()

    def start(self):
        self.socket.bind(self.addr)  # 启动绑定本地地址和端口udp
        threading.Thread(target=self.recv, name='recv').start() #

    def recv(self):
        while not self.event.is_set():
            data, raddr = self.socket.recvfrom(1024)
            logging.info(data)
            logging.info(raddr)
            if data.strip() == b'^hb^':
                continue

            if data.strip() == b'quit':
                if raddr in self.clients:
                    self.clients.remove(raddr)
                continue

            self.clients.add(raddr)
            msg = 'Ack {} .from :{}'.format(data, *raddr).encode()
            for c in self.clients:
                self.socket.sendto(msg, c)

    def stop(self):
        for c in self.clients:
            self.socket.sendto(b'bye',c)
        self.socket.close()
        self.event.set()


if __name__ == '__main__':
    cs = ChatUdpServer()
    cs.start()
    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            cs.stop()
            break
        cs.send(cmd)
        print(threading.enumerate())
        logging.info(cs.clients)
