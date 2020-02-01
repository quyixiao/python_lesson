import datetime
import logging
import random
import threading
import time
# semaphore信号量
# 和Lock很像，信号量对象内部维护一个倒计数器，每一次acquire都会减1，当acquire方法发现计数为0就阻塞请求线程
# 直到其它的线程对信号量release后，计数大于0，恢复阻塞的线程
# Semmaphore(value=1)，构造方法，value小于0，抛出ValueError异常
# acquire(blocking=True,timeout=None)   获取信号量，计数器减1，获取成功返回True
#
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

def worker(s: threading.Semaphore,i :int):
    logging.info(semaphore.__dict__)
    semaphore.acquire()
    logging.info('exit -------------------')

ts = []

semaphore = threading.Semaphore(3)

for i in range(9):
    time.sleep(1)
    t = threading.Thread(target=worker, args=(semaphore,i), name='semaphore-{}'.format(i))
    t.start()
    ts.append(t)

for t in ts:
    t.join()

print('----------------end-------------------')

