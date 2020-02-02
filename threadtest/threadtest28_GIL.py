import datetime
import logging
import random
import threading
import time

from threading import BoundedSemaphore, Semaphore
from queue import Queue

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(20000000):
        sum += 1


ts = []
for i in range(5):
    t = threading.Thread(target=calc, )
    t.start()
    ts.append(t)

for a in ts:
    a.join()

delta = (datetime.datetime.now() - start)
logging.info(delta)
