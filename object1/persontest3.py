
class MyClass:
    def __init__(self):
        print('self in init={}'.format(id(self)))

c = MyClass() # 会调用__init__ 先创建初始化函数
print('c = {}'.format(id(c))) # 再调用




