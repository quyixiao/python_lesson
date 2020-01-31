import logging
import threading
import time
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker():
    for x in range(100):
        time.sleep(0.5)
        logging.info(" {} is running {} ".format(threading.current_thread().name, x))


def worker1():
    time.sleep(2)
    logging.info(" {} is running {} ".format(threading.current_thread().name, 5))


threading.Thread(target=worker1, name='worker-xxx', daemon=False).start()

ts = []
for i in range(1, 6):
    name = "worker-{}".format(i)
    t = threading.Thread(target=worker, name=name, daemon=True)
    ts.append(t)

for t in ts:
    t.start()

logging.info('-------------fin-------------------------')
