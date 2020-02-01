import logging
import threading
import time

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

lock = threading.RLock()


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
