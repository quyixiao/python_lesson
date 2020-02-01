import logging
import threading
import time

# Event 的wait优于time.sleep，它会更快的切换到其他的线程，提高并发效率
# wait 的时间会更加的短，sleep 要更加长的时间
# wait 是不是调用操作系统的函数，sleep 有没有调用sleep 函数
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class Counter:
    def __init__(self):
        self.x = 0
        self.lock = threading.Lock()

    def inc(self):
        time.sleep(0.0001)
        self.x += 1

    def dec(self):
        time.sleep(0.0001)
        self.x -= 1

    @property
    def value(self):
        return self.x


def run(c: Counter, count=100):
    for _ in range(count):
        for i in range(-50, 50):
            if i < 0:
                c.dec()
            else:
                c.inc()
    print('value ---' + str(c.value))


c = Counter()
c1 = 10
c2 = 10
for i in range(c1):
    threading.Thread(target=run, args=(c, c2)).start()

e = threading.Event()
while threading.active_count() > 1:
    e.wait(1)

print(c.value)
