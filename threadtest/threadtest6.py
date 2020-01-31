import threading
# print 线程不安全函数
#

def worker():
    for x in range(100):
        print("{} is {} \n".format(threading.current_thread().name, str(x)), end='')


for i in range(5):
    name = 'worker' + str(i)
    threading.Thread(target=worker).start()
