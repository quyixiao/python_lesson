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

# concurrent.futures
# 异步并行执行编程的模块，提供了一个高级的异步可执行的使得接口
# 提供了2个池执行器
# ThreadPoolExecutor对象
# 首先需要定义一个池的执行器对象，Executor类子类对象
# ThredPoolExecutor(max_workers=1) 池中至多创建max_workers个线程池来同时异步执行返回Executor实例
# submit(fn,*args,**kwargs) 提交执行的函数及其参数，返回Future实例
# shutdown(wait=True) 池清理
# Future类
# done()            如果调用被成功取消或者执行完成，返回true
# canceled()        如果调用被成功的取消，返回True
# running()         如果存在运行且不能被取消，返回True
# cancel()          尝试取消调用，如果已经执行且不能取消返回False,否则返回True
# result(timeout=None) 取返回的结果，timeout为None,一直
# 线程池中的

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
start = datetime.datetime.now()
fs = []

def worker():
    logging.info('begin')
    time.sleep(5)
    logging.info('-------end---------')


executor = futures.ThreadPoolExecutor(max_workers=4)
fs = []
for i in range(3):
    futrue = executor.submit(worker)
    fs.append(futrue)

for i in (3, 6):
    futrue = executor.submit(worker)
    print('--------------------------------')
    fs.append(futrue)

while True :
    time.sleep(2)
    logging.info(threading.enumerate())
    flag = True
    for f in fs :
        logging.info(f.done())
        flag = flag and f.done()

    print('*'*30)
    if flag:
        executor.shutdown()  # 清理池，池中的线程全部杀掉
        logging.info(threading.enumerate())
        break
# 线程池一旦创建了线程，就不需要频繁的清除