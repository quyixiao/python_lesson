import threading
import time  # 线程对象


# start 问操作系统，准备启动一个真正的线程
# run 是运行一个方法
# start 必须在操作系统中开辟一个新的线程，run 只是一个方法
#


def add(x, y):
    print(getthreadinfo() + '--------------------' + ' ' + str(x) + ' ' + str(y) + '---------' + str(x + y))
    return x + y


def getthreadinfo():
    return (' ' + threading.current_thread().name + ' ' +
            threading.main_thread().name + ' ' + str(threading.active_count()) + ' ')


class MyThread(threading.Thread):
    def start(self):
        print('start ')
        super().start()

    def run(self):
        print('run')
        super().run()


t = threading.Thread(target=add, args=(4, 5), name='th1')  # 创建新的线程

if __name__ == '__main__':
    print('3333333333333333333333')
    t.start()  # 123145571459072 th1 MainThread 2 [<_MainThread(MainThread, started 4544503232)>, <Thread(th1, started 123145571459072)>] 123145571459072-------------------- 4 5---------9
    # start 之后，不能run  AttributeError: 'Thread' object has no attribute '_target'
    # t.run() # 4624903616 MainThread MainThread 1 [<_MainThread(MainThread, started 4624903616)>] 4624903616-------------------- 4 5---------9
    # t.run() AttributeError: 'Thread' object has no attribute '_target' 也不能run 之后，再run 方法
    #
