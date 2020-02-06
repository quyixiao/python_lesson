import datetime
from socket import socket
import threading
import logging

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatClient:
    def __init__(self,rip='127.0.0.1',rport=9999):
        self.raddr = (rip,rport)
        self.socket = socket()
        self.event = threading.Event()

    def start(self):
        self.socket.connect(self.raddr)
        threading.Thread(target=self.recv,name='recv').start()

    def recv(self):
        while not self.event.is_set():
            data = self.socket.recv(1024)
            logging.info(data)

    def send(self,msg:str):
        data = "{}\n".format(msg.strip()).encode() # 服务端需要一个换行符
        self.socket.send(data)

    def stop(self):
        self.socket.close()
        self.event.wait(3)
        self.event.set()
        logging.info("client stops ")

def main():
    cc = ChatClient()
    cc.start()

    while True:
        cmd = input('>>>>')
        if cmd.strip() == 'quit':
            break
        cc.send(cmd)
        print(threading.enumerate())


if __name__ == '__main__':
    main()


