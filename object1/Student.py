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
#

