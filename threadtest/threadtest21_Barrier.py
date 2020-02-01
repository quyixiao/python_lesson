import datetime
import logging
import random
import threading
import time

# 有人翻译成栅栏，我建义使用屏障，可以想象成路障，道闸
# Barrier(parties,action=None,timeout=None) 构建Barrier对象，指定参与方数目，timeout是wait方法示指定
# 运行结果看出
# 所有的线程冲到了Barrier前等待，直到parties这个数目
# 所有的线程必需初始化完成后，才能继续工作，例如运行前加载数据，检查，如果这些工作没有完成，就开始运行，将不能正常工作
# 10个线程做10种工作准备，每个线程负责一种工作，只有这10个线程都完成后，才能继续工作，先完成的要等待后完成的线程
# 例如：启动一个程序，需要先加载磁盘文件，缓存预热，初始化连接池等工作，这些工作可以齐头并进，不过只有都满中以后才能
# 继续向后执行的，假设数据连接失败，则初始化工作失败，就要abort,barrier置为broken，所有的线程收到异常退出
# 工作量
# 有10个计算任务，完成了6个，就算工作完成
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker(barrier: threading.Barrier,i :int):
    logging.info('waiting for {} threads.'.format(barrier.n_waiting))
    start = datetime.datetime.now()
    try:
        if i > 2 :
            barrier.abort()

        randomvalue = random.randint(1, 10)
        time.sleep(randomvalue)
        logging.info('exe time {} '.format(randomvalue))
        barrier_id = barrier.wait()
        logging.info('running ' + str(barrier_id) + ", exet = " + (str(datetime.datetime.now() - start)))
    except Exception as e:
        logging.info(str(barrier.broken) + '------------------' + str(i))


ts = []
barrier = threading.Barrier(3)
for i in range(6):
    t = threading.Thread(target=worker, args=(barrier,i), name='bar-{}'.format(i))
    t.start()
    ts.append(t)

for t in ts:
    t.join()

print('----------------end-------------------')
