import datetime
import socket
import threading
import logging
import socketserver

# 上面的例子中，如果客户端断开了，服务端知道了，每一个服务端还需要对所有的客户端发送的数据，包括已经断开的客户端
# 代码改进
# 加一个ack机制和心跳heartbeat，心跳，就是一端定时发往另一端的信息，一般每次数据越少越好，心跳时间间隔写好就好了
# ack即响应，一端收到另一端的消息后返回的信息
# 测试说明
# ThreadingTCPServer是异步的，
# 创建一个服务器需要几个步骤
# 1.从BaseRequestHandler类派生出来的类，并覆盖其handle()方法来创建请求的处理程序类，此方法将处理传入请求
# 2.实例化一个服务器类，传参服务器的地址和请求处理类
# 3.调用服务器实例handle_request()或serve_forever()方法
# 4.调用server_close()关闭套接字

FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class MyHandler(socketserver.BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):
        print(self.request) # new socket 用来recv
        print(self.client_address) # raddr
        print(self.server)
        print(self.__dict__)
        print(self.server.__dict__)


        for i in range(3):
            print(threading.enumerate())
            print(threading.current_thread())
            data = self.request.recvfrom(1024)
            print(data,self.client_address)

    def finish(self):
        pass



server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyHandler)
print(server)
server.serve_forever()
