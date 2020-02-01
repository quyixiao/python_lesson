import logging
import threading
import time

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

lock = threading.RLock()

lock.acquire()
lock.acquire()


def worker(l):
    l.acquire()
    logging.info('in thread ')


t = threading.Thread(target=worker, args=(lock,))
t.start()

threading.Event().wait(2)

logging.info('in main ')
