import time


class Student:

    def __init__(self, name,**kwargs):
        self.__name = name
        self.__scores = kwargs

    def get_score(self):
        return self.__scores

    @property
    def name(self):
        return self.__name


    def __del__(self): # 将自己相关的东西

        print('del')



tom = Student('tom')
jerry = Student('jerry')

del tom
print('------------------')
time.sleep(3)
del jerry
print('=============end======================')
#  实现由于 Python 实现回收机制，不能确定对象
#  内存这个东西不能乱用的
#  数据库连接，清理资源，如果注意资源的清理操作，如果要手动调用的话。
#  Python 没有重载，形式参数， 没有重载，必须，本身就是重载，python 是不需要重载，
#  python 本身就实现了重载，在其他的语言中，不同的函数，有不同的重载方法，在送进来的参数
#

