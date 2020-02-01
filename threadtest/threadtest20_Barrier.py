import datetime
import logging
import random
import threading
import time

# 有人翻译成栅栏，我建义使用屏障，可以想象成路障，道闸
# Barrier(parties,action=None,timeout=None) 构建Barrier对象，指定参与方数目，timeout是wait方法示指定
# 运行结果看出
# 所有的线程冲到了Barrier前等待，直到parties这个数目
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker(barrier: threading.Barrier):
    logging.info('waiting for {} threads.'.format(barrier.n_waiting))
    start = datetime.datetime.now()
    try:
        randomvalue = random.randint(1, 10)
        time.sleep(randomvalue)
        logging.info('exe time {} '.format(randomvalue))
        barrier_id = barrier.wait()
        logging.info('running ' + str(barrier_id) + ", exet = " + (str(datetime.datetime.now() - start)))
    except Exception as e:
        logging.info(e)


ts = []
barrier = threading.Barrier(5)
for i in range(5):
    t = threading.Thread(target=worker, args=(barrier,), name='bar-{}'.format(i))
    t.start()
    ts.append(t)

for t in ts:
    t.join()

print('----------------end-------------------')
