import datetime
import logging
import random
import threading
import time

from threading import BoundedSemaphore, Semaphore
from queue import Queue
# 注意，不要在代码中出现的print等访问的IO语句
# 从两段的python在运行时，保证在同一时刻，只能在同一时刻，
# 由此就引发了一个问题，IO密集型，确实算完了，
# IO密集型是可用的，
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
