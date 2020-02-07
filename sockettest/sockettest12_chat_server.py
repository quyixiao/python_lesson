import datetime
import socket
import threading
import logging
import socketserver
import sys

FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatHandler(socketserver.BaseRequestHandler):
    clients = {} # 记录多个实例

    def setup(self):
        self.event = threading.Event()
        self.clients[self.client_address] = self.request


    def handle(self):
        print(self.request)  # new socket 用来recv
        print(self.client_address)  # raddr
        print(self.server)  # 如果是这样的话，要了解他们
        print(self.__dict__)
        print(self.server.__dict__)

        while not self.event.is_set():
            print(threading.enumerate())
            print(threading.current_thread())
            data = self.request.recvfrom(1024)
            if data == b'' or data == b'quit':
                print('断开....')
                self.event.set()
                break

            print(data ,'============================================')
            print(data, self.client_address)
            msg = "{} .ack\n".format(data).encode()
            for c in self.clients.values():
                c.send(msg)
            print('-----------------while---------end-------------')

    def finish(self):
        self.event.set()
        self.clients.pop(self.client_address)

server = socketserver.TCPServer(('0.0.0.0', 9999), ChatHandler)
print(server)

t = threading.Thread(target=server.serve_forever, name='echoserver')
t.start()

if __name__ == '__main__':
    try:
        while True:
            cmd = input('>>>')
            if cmd.strip() == 'quit':
                server.server_close()
                break
    except Exception as e:
        logging.error(e)
    except KeyboardInterrupt:
        pass
    finally:
        sys.exit(0)
