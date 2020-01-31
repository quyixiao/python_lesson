import logging
import threading

# print 线程不安全函数 ，是线程不安全的，所以，我们要特别注意
# 看代码，应该是一行行打印的，很多的字符打在一起的，为什么
# 说明了print函数被打断了，被线程切换打断了，print函数分成两步，第一步打印字符串，第二步的行，就是这个线程之间
# 字符串是不可变的类型，它可以作为一个整体不可分割的输出，end = '就不让print输出的行'
# 使用Logging
# 标准库里面的logging模块，日志处理模块，线程是安全的，生产环境都使用logging
# daemon线程和non-daemon线程
# 注意： 这里的daemon 不是linux中的守护进程
# 进程靠线程执行代码的，至少有一个主线程，其他的线程是工作的线程
# 主线程是第一个启动的线程
# 父线程：如果线程A中启动了一个线程
#
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def worker():
    for x in range(100):
        logging.info(" {} is running {} ".format(threading.current_thread().name, str(x)))


for i in range(5):
    name = 'worker' + str(i)
    threading.Thread(target=worker, name=name).start()
