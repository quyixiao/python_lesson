import datetime
import logging
import random
import threading
import time
# from multiprocessing import Process
from concurrent import futures
from multiprocessing import Process, Pool

from threading import BoundedSemaphore, Semaphore
from queue import Queue
# 效率还太高了，没有办法
# 该库统一了线程池，进程池调用，简化了编程
# 是Python简单的思想哲学的体现
# 唯一的缺点就是，无法设置线程的名称，但是这个都是不值一提的
# 高效率的库肯定都是异步的

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
start = datetime.datetime.now()
fs = []


def worker():
    logging.info('begin')
    time.sleep(5)
    logging.info('-------end---------')

if __name__ == '__main__':
    #   executor = futures.ProcessPoolExecutor(max_workers=4)
    with futures.ProcessPoolExecutor(max_workers=4) as  executor:
        fs = []
        for i in range(3):
            futrue = executor.submit(worker)
            fs.append(futrue)

        for i in (3, 6):
            futrue = executor.submit(worker)
            print('--------------------------------')
            fs.append(futrue)
        while True:
            time.sleep(2)
            logging.info(threading.enumerate())
            flag = True
            for f in fs:
                logging.info(f.done())
                flag = flag and f.done()
            print('*' * 30)
            if flag:
                logging.info('退出')
                break
        # 线程池一旦创建了线程，就不需要频繁的清除
        logging.info(threading.enumerate())
