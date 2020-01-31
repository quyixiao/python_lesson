import logging
import threading
import time

# 上例说明，如果有non-daemon线程的时候，主线程退出，也不会杀掉
# 如果我在线程内部启动这样的问题的话，
# 在父线程调用我自己，我必需要执行完成，
# join 阻塞，按照我们期望的这样，
# join 不想随便退出，同时，使用join 表示当前线程只能在这里等待，用join ，用
#



FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker():
    time.sleep(0.5)
    logging.info(" {} is running {} ".format(threading.current_thread().name, x))
    t1 = threading.Thread(target=worker1, name='worker-xyz', daemon=True)
    t1.start()
    t1.join()
    print('join--------------------------------')


def worker1():
    time.sleep(8)
    logging.info(" worker1 {} is running {} ".format(threading.current_thread().name, 5))

x = threading.Thread(target=worker)
x.start()

print(threading.enumerate())
logging.info('-------------fin-------------------------')
