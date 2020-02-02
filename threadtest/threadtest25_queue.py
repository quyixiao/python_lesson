import datetime
import logging
import random
import threading
import time

from threading import BoundedSemaphore, Semaphore
from queue import Queue

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


q = Queue() # queue是线程安全的
if q.qsize() > 0 :
    q.get()

if q.qsize() == 1 :
    q.get() # 未必会成功









