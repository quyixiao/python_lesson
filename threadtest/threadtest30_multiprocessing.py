import datetime
import logging
import random
import threading
import time
#from multiprocessing import Process
from multiprocessing import Process

from threading import BoundedSemaphore, Semaphore
from queue import Queue
# 注意，不要在代码中出现的print等访问的IO语句
# 从两段的python在运行时，保证在同一时刻，只能在同一时刻，
# 由此就引发了一个问题，IO密集型，确实算完了，
# IO密集型是可用的，
# 单线程，多线程都跑了4分钟多，而多进程用了1分半，这个真并行
# 可以看出，几乎没有什么学习难度
# 注意：__name__=='__main__' 多进程的代码一定要放在这下面的一行
# 进程间同步
# 进程间同步提供了和线程同步的一样的类，使用方法一样，使用的效果也类似
# 不过，进程间的代价要高于线程间，而且底层实现是不同的，只不过Python屏蔽了这些不同之
# 通信方式
# 多进程就是启动多个解释器进程，进程间的通信必须序列化，反序列化
# 数据的线程安全性问题
# 由于每个进程没有实现多个线程，GIL可以说没有什么用了
# 进程池举例
# 进程创建的代价比线程高得多，如果要
# apply(self,func,args=(),kwds={}) 阻塞执行，导致主进程执行其他的进程就像一个个的执行
# apply_async(self,func,args={},kwds={},callback=None,error_callback=None) 与apply方法的用法是一致的，非阻塞执行，得到的
# 后果会执行回调
# close()       关闭池，池不能再接受新的任务
# terminate()   结束工作进程，不再处理未处理的任务
# join()        主进程阻塞等待子进程的退出，join方法要在close()或terminate之后再使用
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
start = datetime.datetime.now()

def calc():
    sum = 0
    for _ in range(100000000):
        sum += 1

ts = []
if __name__ == '__main__':
    for i in range(5):
        p = Process(target=calc)
        ts.append(p)
        p.start()

    for t in ts:
        t.join()

    delta = (datetime.datetime.now() - start)
    logging.info(delta)
