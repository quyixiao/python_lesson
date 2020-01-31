import logging
import threading
import time
# Timer 本质是一个线程，可以提供了一个cancel()来，执行，
# Timer 的用处好像也没有什么用
# 源码中，
# 线程同步，线程间协同，通过某种技术，让一个线程访问某些数据时，其他的线程不能访问这些数据，直到该线程完成对数据的操作
# 不同的操作系统实现的技术有所不同，有临界区，互斥量，信号量，事情Event等
# Event **
# Event事件，是线程间通信机制中最简单的实现，使用一个内部的标记flag , 通过flag 的True 或False的变化 来进行操作
# 名称            含义
# set ()        标记设置
# clear()       标记设置为False
# is_set()      标记是否为True
# wait(timeout=None) 设置等待标记为True的时长，None为
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

def add(x,y):
    ret = x + y
    logging.info('ret {}'.format(ret))
    return ret


t = threading.Timer(5,add,args=(4,5))
t.setDaemon(True)
t.setName('timer-abc')
print('-------------------')
t.start()
t.join()

print('---------------------')


