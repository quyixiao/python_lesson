import logging
import threading
import time

# 上例说明，如果有non-daemon线程的时候，主线程退出，也不会杀掉
# 如果我在线程内部启动这样的问题的话，
# 在父线程调用我自己，我必需要执行完成，
# join 阻塞，按照我们期望的这样，
# join 不想随便退出，同时，使用join 表示当前线程只能在这里等待，用join ，用
# 使用了join方法后，daemon线程执行完成了，主线程才退出了
# join(timeout=None) ，是线程的标准方法之一
# 一个线程中调用另一个线程的方法，join方法，调用者将被阻塞，直到被调用线程终止
# 一个线程可以被join多次
# timeout参数指定调用者等待多久，没有设置超时，就一直等到被调用线程结束，调用谁的join方法，就join谁，就要等谁
# daemon线程应用场景
# 简单来说就是
# 本来没有daemon thread ，为了简化程序员的工作，让他们不用去记录和管理那些后台线程，创造一个daemon thread 的概念
# 这个概念唯一的作用就是，当你把一个线程设置daemon，它会随着主线程退出而退出
# 主要的应用场景
# 后台服务，如发送心跳包，监控，这种场景最多
# 主线程工作才有用的线程，如主线程中维护这个公共的资源，主线程已经清理了，准备退出，而工作线程使用这些资源工作也没有意义了
# 一起退出最合适
# 3.随时可以被终止的线程
# 如果主线程退出，想所有的其他的工作一起退出，就使用daemon=True来创建工作线程
# 比如，开启一个线程定时判断WEB服务是否正常工作，主线程退出，工作线程也没有必要的存在了，应该随着主要和退出一起退出，
# 这种daemon线程一旦创建，就可以忘记它了，只用关心主要线程时候退出就行了
# 要保证所有的时间必需是一样的，时间的函数，只要业务，就肯定和时间是有关系的，记录时间也是
# 随时可以被终止的线程
# 如果主要和退出，想所有的其他工作线程一起退出，
# daemon线程，简化了程序员手动关闭线程的工作
# 如果在non-daemon线程A中，对另一个daemon线程B使用了join方法，这个线程B设置成daemon
# 如果在一个daemon线程c中，对另一个daemon线程D使用了join方法，只能说明c在等待D,主线程退出，C和D不管是否结束
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
