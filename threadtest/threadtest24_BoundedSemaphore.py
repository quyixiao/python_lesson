import datetime
import logging
import random
import threading
import time

from threading import BoundedSemaphore

# semaphore信号量
# 对于类似资源的使用的情况，我们一般用来做
# 代价非常的高，
# 上例子中，BoundSemaphore类，有界的信号量，不允许使用release超出初始值的范围，否则，抛出ValueError异常
# 将上例中信号量改成有界的信号量试一试
# 应用举例
# 连接池
# 因为资源有限，且开启一个连接成本高，所以，使用连接池
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker(s: threading.Semaphore, i: int):
    logging.info(semaphore.__dict__)
    with semaphore:
        pass
    semaphore.release()
    logging.info('exit -------------------')


ts = []

semaphore = threading.BoundedSemaphore(3)

for i in range(9):
    time.sleep(1)
    t = threading.Thread(target=worker, args=(semaphore, i), name='semaphore-{}'.format(i))
    t.start()
    ts.append(t)

for t in ts:
    t.join()


def worker1(sema: threading.Semaphore):
    value = sema._value
    for i in range(value):
        sema.acquire()
        logging.info("{} {} ".format(i, sema.__dict__))



t = threading.Thread(target=worker1, args=(semaphore,))
t.start()
t.join()

print(semaphore.__dict__)

print('----------------end-------------------')
