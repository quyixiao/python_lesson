import sys
import time


# 上下文管理的安全性
# with 语法只能保证在进入和退出的时候保证进入的时候 enter ，出来的时候 exit
# 为加法函数计时
# 方法1 ： 使用装饰器显示该函数的执行时长
# 方法2 ： 能不能用上下文管理来实现执行时长

class A:
    def __init__(self, name):
        print('init')
        self._name = name

    def __enter__(self):
        print('enter ')
        return self._name

    def __exit__(self, exc_type, exc_val, exc_tb): #如果返回一个为 True 则压制异常
        print('exit+++++++++++++++++++', exc_type, "|", exc_val, '|', exc_tb)

    @property
    def name(self):
        return self._name

    def __str__(self):
        return "my name is {}".format(self._name)


f = A('bbbbbbbbb')
print('------------++++++++++++++++', f)
with  f:
    # raise  Exception('exception ')
    # sys.exit(-1) # 即使程序有问题，还是不变，我们已经看到了
    #
    print('-----------------')
    print(f)

print('==================================================')
with A('jerry') as f:
    #raise KeyError('异常')
    print(f)
