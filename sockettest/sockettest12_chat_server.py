import datetime
import socket
import threading
import logging
import socketserver
import sys
# 通过打印可以看到，
# 总结，为每一个连接提供RequestHandlerClass类实例，依次调用setup,handle,finish方法，且使用了try...finally结构
# 保证finish方法一定被调用，这些方法依次执行完成，如果想维持这个连接和客户端通信，就需要在handle函数中使用循环
# socketserver模块提供了不同的类，但是编程接口都是一样的，即使是多进程，多线程也是一样的，大大的减少了编程的难度
# 这就是框架的好处，看似解放了我们，但是，这就是python 中的简单
# 异步编程
# 重要的概念
# 同步，异步
# 阻塞，非阻塞
# 区别
# 联系
# 同步IO,异步IO,
# 异步编程
# 重要的概念
# 同步，异步
# 函数或方法被调用的时候，调用者是否得到最终的结果
# 直接得到的最终结果的，就是同步调用
# 不直接得到的结果，就是异步调用
# 同步就是让我们打饭，你不打好，我就不走开，直到你打饭给我
# 异步就是让你打饭，打不着，我不等你，但是我会盯着你，你手机密码，我就会过来拿走，异步并不保证时间多长最终打完饭
# 阻塞，非阻塞
# 函数或方法调用的时候，是否立刻返回
# 立即返回就是阻塞调用
# 区别
# 同步，异步，与阻塞，非阻塞不相关
# 同步与异步区别在于，调用者是否得到了想要 的最终结果
# 同步就是一直要执行到返回的最终结果
# 异步就是直接返回了，但是返回的不是最终结果，调用者不能通过这种调用得到结果，还要通过被调用者，使用其它的方式通知调用者
# 来取回最终结果
# 阻塞与非阻塞的区别在于，调用者是否还能干其他的事情
# 阻塞，调用者就只能干等
# 非阻塞，调用者可以先去心会别的事情，不用一直等
# 联系
# 同步阻塞，我啥事都不干，就等你打饭给我，打到饭的结果，而且我啥事也不做，同步加阻塞
# 抛出异常
# 同步IO,异步IO,IO多路复用
# IO两个阶段
# IO过程分成两个阶段
# IO过程分成两个阶段
# 1.数据准备阶段
# 2.内核空间复制到用户进程缓冲区阶段
# 发生IO的时候
# 内核从输入设备读取，写数据，（淘米，把米放到饭锅里煮饭）
# 进程从内核复制数据（盛饭，从内核这个饭锅里把饭装到碗里来）
# 系统调用,read函数
# IO模型
# 同步IO
# 同步IO模型包括阻塞IO,非阻塞IO,IO多路复用
# 进程调用read操作，如果IO设备没有准备好，立即返回Error,进程不阻塞，用户可以再次发起系统调用，如果内核准备好了，就阻塞，
# 然后复用数据用用户空间
# 第一阶段，
# 所谓IO多路复用，就是同时监控多个IO,有一个准备好了，就不需要等了了，开始处理，提高同时处理IO的能力
# select几乎所有的操作系统支持，Poll是对select的升级
# epoll，Linux系统内核，2.5开始支持，对select和poll的增强，在监视的基础上，看着办吧回调机制，BSD,MAC平台有kqueue，Windows有iocp
# select举例，食堂供应很多的菜（众多的IO）,你需要吃某三菜一汤，大师傅（操作系统）说要现做，需要等，你只好等待，其中的一样菜好了
# ，大师傅你过来说点好的菜就好了，你得自己找找看看，哪一样才好了，请服务员把做好了菜打给你
# epoll是有菜准备好了，大师傅喊你去账号容器直接打菜，不用自己找菜了
# python 的select库
# 实现了select，poll系统调用，这个基本上操作系统都支持，部分实现了epoll
# 底层的IO多路复用模块
# 开发中的选择
# 1.完全跨平台，使用select，poll，但是性能比较的差
# 2.针对不同的操作系统自行选择的技术，这样做会提高处理的性能
# select库
# 类层次结构
# BaseSelector :
# +--SelectSelector 实现select
# +--PolllSelector  实现poll
# +--EpollSelector  实现epoll
# +--DevpollSelector 实现devpoll
# +--KqueueSeletor  实现kqueue
# selectors.DefaultSelector返回平台最有效，性能最高的实现
# 但是，由于没有实现Windows下的IOCP,所有，只有退化为select
# 

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
