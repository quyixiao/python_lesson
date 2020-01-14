# 随机整数生成的类
# 可以指定一批生成的个数，可以指定数值范围，可以高速每批生成数字的个数
import random


class RandomInt:
    def __init__(self,count = 10,start = 1 ,stop = 100):
        self.count = count
        self.start = start
        self.stop = stop


    def genint(self):
        return [random.randint(self.start,self.stop) for _ in range(self.count)]


class Utils:
    @classmethod
    def genint(cls,count=10,start=1,stop=100):
        return [random.randint(start,stop) for _ in range(count)]



class RandomGenerator:
    def __init__(self,count = 10,start = 1,stop = 100):
        self.count = count
        self.start = start
        self.stop = stop
        self._gen = self.__generator()

    def __generator(self):
        while True:
            yield random.randint(self.start,self.stop)


    def generator(self):
        return [next(self._gen) for _ in range(self.count)]





class RandomGenerator1:
    def __init__(self,count = 10,start = 1,stop = 100):
        self.count = count
        self.start = start
        self.stop = stop
        self._gen = self.__generator()

    def __generator(self):
        while True:
            yield [random.randint(self.start,self.stop) for x in range(self.count)]

    def generator(self,count = 10):
        self.count = count
        return next(self._gen)

ri = RandomGenerator1()
print(ri.generator(20))




