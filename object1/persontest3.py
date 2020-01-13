
class MyClass:
    def __init__(self):
        print('self in init={}'.format(id(self)))

c = MyClass() # 会调用__init__ 先创建初始化函数
print('c = {}'.format(id(c))) # 再调用




# 对象属性和操作
#  实例变量是每一个实例自己的变量，是自己独有的，类变量是类的变量，是类的所有实例共享的属性和方法
#  __name__对象名
# __class__ 对象的类型
# __dict__对象的属性的字典
# __qualname__类的限定名


