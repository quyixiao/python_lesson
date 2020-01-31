import logging
import threading
import time
# 上例使用多线程，每个线程完成不同的计算任务
# x是全局变量，可以看出每一个线程的x是独立的，互不干扰，为什么呢？
# 能不能改成全局变量，或者全局函数呢？
# python提供了threading.local类，将这个类的
# 每一个线程中都，本质，运行时，threading.local实例处在不同的线程中，就从大字典中找到当前线程相关的键值
# 对中的字典，覆盖threading.local实例的__dict__
# 这样就可以在不同的线程中，安全的使用线程独有的数据，做到线程的数据隔离，
# 如本地变量一样的安全
# 定义一个变量就可以了，根据不同的线程来实现
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
#
global_data = threading.local()
global_data.x = 100
print(global_data)


def worker(o,i):
    o.x = 1000 * i
    for _ in range(100):
        time.sleep(0.009)
        o.x += 1
    logging.info(o.x)


for i in range(5):
    threading.Thread(target=worker, args=(global_data,i)).start()

while threading.active_count() > 1:
    time.sleep(1)

print(global_data.x)