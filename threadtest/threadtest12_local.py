import logging
import threading
import time

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class A:
    def __init__(self):
        self.x = 0


a = A()


def worker(o):
    for _ in range(100):
        time.sleep(0.009)
        o.x += 1
    logging.info(o.x)



for i in range(5):
    threading.Thread(target=worker, args=(a,)).start()
