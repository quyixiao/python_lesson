import datetime
import logging
import random
import threading
import time
# from multiprocessing import Process
from multiprocessing import Process, Pool

from threading import BoundedSemaphore, Semaphore
from queue import Queue
# 请求应用
# 请求/应答模型，WEB应用中常见的处理模型
# master 启动多个worker工作进程，一般和CPU数目相同，发挥多核优势
# worker工作进程中，往往需要操作网络IO和磁盘IO,启动多线程，提高并发处理能力，worker处理用户的请求
# ，往往需要等待数据，处理完成请求还通过网络IO返回响应
# 这就是nginx工作模式
# 绑定的目的就是缓存
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(100000000):
        sum += 1




if __name__ == '__main__':
    pool = Pool(5)
    for i in range(5):
        pool.apply_async(calc)  # 异步方法

    pool.close()
    pool.join()

    delta = (datetime.datetime.now() - start)
    logging.info(delta)
