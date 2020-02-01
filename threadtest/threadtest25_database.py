import datetime
import logging
import random
import threading
import time

from threading import BoundedSemaphore, Semaphore

# 先拿的，拿到了就拿到了，没有拿到，就没有拿到的
# 假设一种极端的情况，
# 正常的使用分析，正常的信号量，都会先获取信号量，然后用完归还
# 创建很多的线程，都去获取信号量，没有获取信号量的线程阻塞，能归还的线程都是前面的获取到的信号量的线程，其他的
# 没有获取线程都阻塞着，非阻塞的线程append后才release，这个时候，等待的线程将被唤醒，才能pop,也就是没有获取信号量就
# 不能pop，这是线程安全
# 经过上面分析，信号量比计算列表的长度好，线程安全
# 信号量和锁
#




FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

class Connection:
    def __init__(self, name):
        self.name = name


class Pool:

    def __init__(self, count: int):           # 3
        self._value = count
        self.count = count
        self.pool = [self._connection('{}'.format(i)) for i in range(count)]  # 预先加载
        self.sema = Semaphore(count)

    def _connection(self, name):
        # 省略
        return Connection(name)


    def get_conn(self):
        # 从池中拿走一个连接
        self.sema.acquire()
        #
        return self.pool.pop()

    def return_conn(self,conn:Connection):
        if self._value < self.count :
            # self.sema.release() #错的
            # 向池中添加一个连接，
            self.pool.append(conn)
            self.sema.release()



















