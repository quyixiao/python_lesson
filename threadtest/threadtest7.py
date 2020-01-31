import logging
import threading

# print 线程不安全函数 ，是线程不安全的，所以，我们要特别注意
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker():
    for x in range(100):
        logging.info(" {} is running {} ".format(threading.current_thread().name, str(x)))


for i in range(5):
    name = 'worker' + str(i)
    threading.Thread(target=worker, name=name).start()
