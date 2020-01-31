import logging
import threading
import time
# Timer 本质是一个线程，可以提供了一个cancel()来，执行，
# Timer 的用处好像也没有什么用
# 源码中，
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

def add(x,y):
    ret = x + y
    logging.info('ret {}'.format(ret))
    return ret


t = threading.Timer(5,add,args=(4,5))
t.setDaemon(True)
t.setName('timer-abc')
print('-------------------')
t.start()
t.join()

print('---------------------')


