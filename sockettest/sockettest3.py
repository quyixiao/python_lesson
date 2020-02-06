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
            f = s.makefile(mode='rw')
            logging.info(f)
            logging.info(addr)
            logging.info(f.fileno())
            self.clents[addr] = f
            threading.Thread(target=self.recv, name='recv', args=(f, addr)).start()

    def recv(self, f, addr):
        while not self.event.is_set():
            try:
                data = f.readline()
                logging.info(data)
            except Exception as e:
                logging.error(e)
                data == 'quit'

            if data == 'quit':
                self.clents.pop(socket.getpeername())
                socket.close()
                break

            msg = "ack {} {}".format(
                addr,
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                data)

            for s in self.clents.values():
                f.write(msg)
                f.flush()

    def stop(self):
        for s in self.clents.values():
            s.close()
        self.socket.close()
        self.event.set()


if __name__ == '__main__':
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input(">>>>")
        if cmd.strip() == 'quit':
            cs.stop()
            threading.Event.wait(3)
            break
        logging.info(threading.enumerate())
