class Base:
    n = 2

class Point(Base):
    def __init__(self,x,y):
        print('+++++++++++++++++++++++++++++++')
        self.x = x
        self.y = y
        print('**********************************')
    # 找不到时候，就可以用了
    def __getattr__(self, item): #如果没有定义这个方法，就定义属性异常，如果找不到，则调用他
        print(item,'------------------')
        #print(getattr(self,'x'),'==========================')
        #setattr(self,item,'654321')
        #  如果属性没有，则直接找，属性异常的时候，异常被吃掉了，这个就是后悔药，只要给你一下函数，你就能做很多的事情
        # print(self.z5 ,'+++++++++++++++++++++++++===') # RecursionError: maximum recursion depth exceeded while calling a Python object
        #return getattr(self,item)
        return '123456'

    def __setattr__(self, key, value):
        if key == 'x':
            value = 6
        print('__setattr__',key,value)
        self.__dict__[key] = value



    def __delattr__(self, item):
        print('删除属性','del {}'.format(item))


p = Point(4,5)
print(p.x,p.y )
#print(p.__dict__)
#print(p.z )
#print(p.z )
#print(p.__dict__)


print('==============================')
print(p.n)
# print(Point.A) # AttributeError: type object 'Point' has no attribute 'A'

del p.z

p.n = 200
print(p.n )



print(10,p.__dict__)
print(super(Point,Point).n) # 可以拿到
print(type(p).__base__.__dict__)
print(getattr(Base,'__dict__'))
print(Base.__dict__)
# 如果在里面用 set dict 就可以了
# 可以阻止通过实例来删除属性来操作，通过属性可以访问，
# 可以将一个类当作函数来看，只要可调用，我们就可以在后面加一个对象，具有反射能力的函数，type(),isinstance(),callable()
# dir(),getattr() ,如何将一个装饰器
# 结合上下文是一个非常有用，资源当做文件来看，类，上下文管理，如何实现上下文管理，拿一个类
#  具有反射能力的函数有，type(),isinstance(),callable(),dir(),
# 可以设置属性
# 和反射相关的
# 魔术方法
# 这三个魔术方法，
# 我们通过实例来实现，getattr()
# 我们对属性的方法，通过 getattr 来实现
# 将前面的链表，封装成容器
# 要求
# 提供__getitem__,__iter__,__setitem__方法
# 使用一个列表，辅助完成上面的方法
# 进阶，不使用列表，完成上面的方法
# 能够在进行时获取类型信息，能获取到，进行时
# getattr(object,name,[,default]) 通过 name返回 object 的属性值，当属性不存在，将使用 default 来返回，
# 思考
# 这种动态增加属性的方式和装饰器修饰一个类，Mixin 方式的差异
# setattr(object,name,value) object 属性的存在，则覆盖，不存在，则新增
# hasattr(object,name) 决断对象是否有这个名字的属性，name 必须为字符串
# 用上面的方法来修改上例的代码
# 我可以将一个字符串解析成一个代码，通过名称来找到对应的
#


