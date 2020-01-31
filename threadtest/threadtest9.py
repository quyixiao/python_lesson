import logging
import threading
import time

# 上例说明，如果有non-daemon线程的时候，主线程退出，也不会杀掉
# 如果我在线程内部启动这样的问题的话，
#



FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker():
    for x in range(100):
        time.sleep(0.5)
        logging.info(" {} is running {} ".format(threading.current_thread().name, x))


def worker1():
    time.sleep(3)
    logging.info(" {} is running {} ".format(threading.current_thread().name, 5))


t1 = threading.Thread(target=worker1, name='worker-xyz', daemon=True)
t1.start()

ts = []
for i in range(1, 6):
    name = "worker-{}".format(i)
    t = threading.Thread(target=worker, name=name, daemon=True)
    ts.append(t)

for t in ts:
    time.sleep(1)
    t.start()

t1.join()
print(threading.enumerate())
logging.info('-------------fin-------------------------')
