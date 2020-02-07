import datetime
import socket
import threading
import logging
import socketserver

# 上面的例子中，如果客户端断开了，服务端知道了，每一个服务端还需要对所有的客户端发送的数据，包括已经断开的客户端
# 代码改进
# 加一个ack机制和心跳heartbeat，心跳，就是一端定时发往另一端的信息，一般每次数据越少越好，心跳时间间隔写好就好了
# ack即响应，一端收到另一端的消息后返回的信息
#

FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request) # new socket 用来recv
        print(self.client_address) # raddr
        print(self.server)
        print(self.__dict__)


server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyHandler)
print(server)
server.serve_forever()

