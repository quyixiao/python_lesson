from pathlib import Path

class A:
    XXX = "8932"
    def __init__(self):
        self.ab = 'ab '
        print('+++++++++++++++++++++++++')

    def __dir__(self) :
        return [1,2,3]


print(dir())
#__dir__返回或者对象的所有的类的信息，尽可能的收集，
# dir() 对于不同类型的对象具有不同的行为
#
print(sorted(dir(A)))
print(sorted(dir(A())))

print(__file__)

print(Path(__file__).parent)
# 魔术方法
#  分类
# 创建，初始化与销毁
# __init__ 与 __del__
# hash
# bool
# 可视化
# 运算符重载
# 容器和大小
# 可调用对象
# 上下文管理
# 反射
# 描述器
# 其他的杂项
#