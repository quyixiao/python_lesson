import logging
import threading
import time

# Event 的wait优于time.sleep，它会更快的切换到其他的线程，提高并发效率
# wait 的时间会更加的短，sleep 要更加长的时间
# wait 是不是调用操作系统的函数，sleep 有没有调用sleep 函数
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class MyTimer:
    def __init__(self, interval, function, args=None, kwargs=None, name=None, *, daemon=None):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.name = name
        self.daemon = daemon
        self.event = threading.Event()
        self.thread = threading.Thread(target=self.run, args=self.args, kwargs=self.kwargs,
                                       name=self.name, daemon=self.daemon)

    def start(self):
        self.thread.start()

    def cancel(self):
        self.event.set()

    def run(self):
        self.event.wait(self.interval)
        if not self.event.is_set():
            self.function(*self.args, **self.kwargs)
        self.event.set()
