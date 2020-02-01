import logging
import random
import threading
import time

# 可重入锁，与线程相关，可在一个线程中获取锁，并可继续在同一个线程中不阻塞获取锁，当锁示释放完
# 其他的线程获取就会阻塞，直到当前线程持有锁的线程释放完成
# Condition
# 构造方法Condition(lock=None)，可以传入一个Lock或者RLock对象，默认是RLock
# acquire           获取锁
# wait(self,timeout=None) 等待或超时
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
lock = threading.RLock()


class Dispatcher:
    def __init__(self):
        self.data = None
        self.event = threading.Event()
        self.send = threading.Event()

    def produce(self, total):
        for _ in range(total):
            data = random.randint(0, 100)
            logging.info(data)
            self.data = data
            self.send.set()
            self.event.wait(1)
        self.event.set()

    def consume(self):
        while not self.event.is_set():
            self.send.wait()
            data = self.data
            logging.info('revived {}'.format(data))
            self.send.clear()
            self.event.wait(0.5)


d = Dispatcher()
p = threading.Thread(target=d.produce, args=(10,), name='producer')
c = threading.Thread(target=d.consume, name='consumer')
p.start()
c.start()
