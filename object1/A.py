import random

#  如果 dir ()
#  分类
#  创建，初始化与销毁
#  __init__与__del__
# hash
# bool
# 可视化
# 运算符的重载
# 容器的大小
# 可调用对象
# 上下文管理
# 反射
# 
class A:
    def __init__(self, name='tom', age=18):
        self.name = name
        self.age = age

    def __hash__(self):
        # return random.randint(1,10000)
        return 1

    def __eq__(self, other):
        print(self.name, other.name)
        print(self.age, other.age)
        return self.age == other.age

    def __repr__(self):
        return "<A name={} ,age={}>".format(self.name, self.age)


# 每一次都是一样的
# print(hash(A))
# print(hash(A))
#
# print(hash(A('zhangsan',10)))
# print(hash(A('lisi',20)))

item = [A(), A()]
print(item)

item = (A(), A())

print(item)

item = {A(), A(30)}

print(item)

# hash 只是计算has 上 值的问题，解决的是存在什么地方，hash 的
# 去重，用到 _eq_方法
# 思考：
# list 类的实例为什么不可 hash ?
#
