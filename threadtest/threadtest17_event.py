import logging
import threading
import time

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

event = threading.Event()


def worker(ret: list, count=10):
    cups = []
    while len(cups) < 10:
        time.sleep(0.5)

        cups.append(1)
        logging.info(threading.current_thread().name + '创建一个值 ' + str(len(cups)))
    # 设置中间变量
    event.set()


def boss():
    logging.info('I am boss ,I am waiting for U.')
    # 等待
    # while not flag :
    #       time.sleep(0.5)
    logging.info(event.wait())
    logging.info('Good job.')


t = threading.Thread(target=worker, args=(10,))
t.start()

b = threading.Thread(target=boss(),name='boss')
b.start()



logging.info(event.wait()) # 只要你们使用同一个event对象，则可以使用


print('----------------finished------------------------')
