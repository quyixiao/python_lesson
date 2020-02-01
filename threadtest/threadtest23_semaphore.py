import datetime
import logging
import random
import threading
import time

# semaphore信号量
# 对于类似资源的使用的情况，我们一般用来做
# 代价非常的高，
#
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker(s: threading.Semaphore, i: int):
    logging.info(semaphore.__dict__)
    with semaphore:
        pass
    semaphore.release()
    logging.info('exit -------------------')


ts = []

semaphore = threading.Semaphore(3)

for i in range(9):
    time.sleep(1)
    t = threading.Thread(target=worker, args=(semaphore, i), name='semaphore-{}'.format(i))
    t.start()
    ts.append(t)

for t in ts:
    t.join()



def worker1(sema: threading.Semaphore):
    value = sema._value
    for i in range(value):
        sema.acquire()
        logging.info("{} {} ".format(i,sema.__dict__))

t = threading.Thread(target=worker1,args=(semaphore,))
t.start()
t.join()

print(semaphore.__dict__)

print('----------------end-------------------')
