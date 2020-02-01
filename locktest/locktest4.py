import logging
import threading
import time

# Event 的wait优于time.sleep，它会更快的切换到其他的线程，提高并发效率
# wait 的时间会更加的短，sleep 要更加长的时间
# wait 是不是调用操作系统的函数，sleep 有没有调用sleep 函数
# 锁的应用场景
# 锁适用于访问和修改同一个共享资源的时候，即读写同一个资源的时候
# 如果全部都是读取同一个资源需要的时候
# 不需要，因为这个时，可以认为共享的资源是不可变的，每一次读取它的值的时候，所有不用加锁
# 使用锁的主要注意事项
# 少用锁，必要的时用锁，使用了锁，多线程访问被锁的资源时，就成了串行，要么排队执行，要么争抢执行
# 举例：
# 加锁时间越短越好，不需要立即释放锁
# 一定要避免死锁
# 不使用锁，有了效率，但是结果是对的
# 所以，我们为了效率要错误的结果是对的
# 所以，我们是为了效率，要正确的结果，让计算机去计算吧
# 可重入锁

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

class Counter:
    def __init__(self):
        self.x = 0
        self.lock = threading.Lock()

    def inc(self):
        time.sleep(0.0001)
        try:
            self.lock.acquire()
            self.x += 1
        finally:
            self.lock.release()

    def dec(self):
        time.sleep(0.0001)
        try:
            self.lock.acquire()
            self.x -= 1
        finally:
            self.lock.release()


    @property
    def value(self):
       with self.lock:
           return self.x

def run(c: Counter, count=100):
    for _ in range(count):
        for i in range(-50, 50):
            if i < 0:
                c.dec()
            else:
                c.inc()
    print('value ---' +str( c.value))

c = Counter()
c1 = 10
c2 = 10

for i in range(c1):
    threading.Thread(target=run, args=(c, c2)).start()

e = threading.Event()
while threading.active_count() > 1:
    e.wait(1)

print(c.value)
