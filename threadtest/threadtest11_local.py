import logging
import threading
import time

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

x = 5

def worker():
    global x
    for _ in range(1000):
        time.sleep(0.0002)
        x = x + 1
    logging.info(x)


def worker1():
    worker()


for i in range(5):
    threading.Thread(target=worker1).start()
