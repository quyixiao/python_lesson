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
# 生产，消费者等待数据，如果生产者准备好了，会
# 为什么让消息者起来，生产
# 消息者先起来，统计学的角度来说，数据影响不大，通知两个，一对二来说
# 上例中，程序本身不是线程安全的，程序逻辑有很多的瑕疵，但是可以很好的帮助我们理解问题
# Condition总结
# Condition用于生产者消费者模型中，解决生产者消费者速度匹配问题
# 使用方式，使用Condition ，必须先acquire,用完了要release,因为内部使用了锁，l默认使用RLock锁，最好的方式是使用with
# 上下文
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
lock = threading.RLock()


class Dispatcher:
    def __init__(self):
        self.data = None
        self.event = threading.Event()
        self.conditon = threading.Condition()


    def produce(self, total):
        for _ in range(total):
            with self.conditon:
                data = random.randint(0, 100)
                logging.info(data)
                self.data = data
                #self.conditon.notify_all()
                self.conditon.notify(2)
            self.event.wait(1)
        self.event.set()

    def consume(self):
        while True:
            with self.conditon:
                self.conditon.wait()
                data = self.data
                logging.info('revived {}'.format(data))
            self.event.wait(0.5)

d = Dispatcher()
for _ in range(5):
    threading.Thread(target=d.consume, name='consumer').start()



for _ in range(1):
    threading.Thread(target=d.produce, args=(10,), name='producer').start()


