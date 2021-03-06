import logging
import threading
import time

# Event 的wait优于time.sleep，它会更快的切换到其他的线程，提高并发效率
# wait 的时间会更加的短，sleep 要更加长的时间
# wait 是不是调用操作系统的函数，sleep 有没有调用sleep 函数
#
FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
lock = threading.Lock()

print(lock,id(lock))

with lock as f :
    print(f,id(f))