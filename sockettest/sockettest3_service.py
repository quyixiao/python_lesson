import datetime
from socket import socket
import threading
import logging

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
# 网络编程
# AF_INET       IPV4
# AF_INET6      IPV6
# AF_UNIX
# TCP 服务端编程
# 服务器编程序骤
# 创建Socket对象
# 绑定IP地址Address和端口Port,bind()方法IPv4地址为一个元组（"IP地址字符串",Port）
# 开始监听
# 上例accept和recv是阻塞的，主线程经常被阻塞而不能工作，怎么办？
# 练习一一写一个群聊程序
# 需求分析
# 聊天工具是CS程序，在此基础上进程扩展
# 程序还是在瑕疵的，
# socket.sendfile(file,offset=0,count=None) 发送一个文件直到EOF,使用高性能的os.sendfile机制，返回发送的字节数
# 如果win下不支持sendfile,或者不是普通的文件，使用send发送文件，offset告诉起始位置，3.5版本开始
#
#

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
