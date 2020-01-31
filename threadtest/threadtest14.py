import logging
import threading
import time
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

def add(x,y):
    ret = x + y
    logging.info('ret {}'.format(ret))
    return ret


t = threading.Timer(5,add,args=(4,5))
#t.setDaemon(True)
t.setName('timer-abc')
print('-------------------')
t.start()
print('---------------------')


