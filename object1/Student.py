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


    def __del__(self):
        print('del')



tom = Student('tom')
jerry = Student('jerry')

del tom
print('------------------')
time.sleep(3)
print('=============end======================')

