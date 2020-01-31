import threading
import time  # 线程对象


# start 问操作系统，准备启动一个真正的线程
# run 是运行一个方法
# start 必须在操作系统中开辟一个新的线程，run 只是一个方法
# 到操作系统中创建了一个线程，先start 启动线程，然后调用run 方法，执行函数
# 使用start 方法启动线程,启动了一个新的线程，名字叫做worker运行，但是使用run方法的，并没有启动新的线程，
# 就是在主线程中调用了一个普通的函数而已
# 因此，启动线程请使用start方法，才能启动多个线程
# 在不同的线程之内，下一个函数调用，
# run 方法不会开启所有的线程， 多线程在单个cpu 上是一个假象，多线程是并发的，
# 在同一时刻，有新的线程，就别当别论，run 方法，和我们的start 方法，
# 创建线程对象，
# 没有开新的线，就是普通的函数调用，所以执行完t1.run()，然后执行t2.run()，这里就不是多线程
# 当使用start方法启动线程后，进程内有多个活动的线程并行工作，就是多线程
# 一个进程至少有一个线程，并作为程序的入口，
#

def add(x, y):
    print(getthreadinfo() + '--------------------' + ' ' + str(x) + ' ' + str(y) + '---------' + str(x + y))
    return x + y


def getthreadinfo():
    return (' ' + threading.current_thread().name + ' ' + threading.main_thread().name)


class MyThread(threading.Thread):
    def start(self):
        print('start ')
        super().start()

    def run(self):
        print('run')
        self._target(*self._args, **self._kwargs)


t = MyThread(target=add, args=(4, 5), name='th1')  # 创建新的线程
if __name__ == '__main__':
    print('3333333333333333333333')
    t.start()
    t.run()
    t.run()
