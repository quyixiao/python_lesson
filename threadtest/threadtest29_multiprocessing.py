import datetime
import logging
import random
import threading
import time

from threading import BoundedSemaphore, Semaphore
from queue import Queue
from multiprocessing.pool import Pool

# 多进程
# 由于Python的GIL,多线程未必是CPU密集型程序的好的选择
# 多进程可以完全独立的的进程环境中运行程序，可以充分的利用多处理器
# 但是进程本身的隔离带来的数据不共享也是一个问题，而线程比进程更加的轻量级
# multiprocessing
# Process类
# Process 类遵循了Thread类的API，减少了学习的难度
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
start = datetime.datetime.now()


class Process(object):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        self.name = name
        self.daemon = False
        self.authkey = None
        self.exitcode = None
        self.ident = 0
        self.pid = 0
        self.sentinel = None

    def run(self):
        pass

    def start(self):
        pass

    def terminate(self):
        pass

    def join(self, timeout=None):
        pass

    def is_alive(self):
        return False
