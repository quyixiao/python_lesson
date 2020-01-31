import logging
import threading
import time

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker(ret: list, count=10):
    cups = []
    while len(cups) < 10:
        time.sleep(0.5)

        cups.append(1)
        logging.info(threading.current_thread().name + '创建一个值 ' + str(len(cups)))
    ret.append(cups)
r = []
t = threading.Thread(target=worker, args=(r,))
t.start()
t.join()
print(r)

print('---------------------')
