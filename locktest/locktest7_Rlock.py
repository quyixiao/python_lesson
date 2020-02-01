import logging
import threading
import time

# 可重入锁，与线程相关，可在一个线程中获取锁，并可继续在同一个线程中不阻塞获取锁，当锁示释放完
# 其他的线程获取就会阻塞，直到当前线程持有锁的线程释放完成
# Condition
# 构造方法Condition(lock=None)，可以传入一个Lock或者RLock对象，默认是RLock
# acquire           获取锁
# wait(self,timeout=None) 等待或超时
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
lock = threading.RLock()

#

def worker(l):
    logging.info('in thread  start ')
    with l:
        with l:
            pass
    time.sleep(5)
    logging.info('in thread ')


t = threading.Thread(target=worker, args=(lock,))
t.start()

threading.Event().wait(2)
logging.info('--------------------------------- ')
lock.acquire()

logging.info('in main ')
