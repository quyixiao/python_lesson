class A :
    def __init__(self):
        self.f = None

    def __enter__(self):
        self.f = open('test')
        return self



# 运行时动态增加属性的方式和装饰器修饰一个类，Mixin 方式的差异
# 这种动态的增加属性的方式是运行时改变的或者实例的方式，但是闭包器或者 Minx 都是定义就决定了，因此反射能力具体更加的灵活性
#


class Base :
    n = 0

class Point(Base):
    z = 6
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __getattr__(self, item):
        return 'missing {} '.format(item)
    # 当你访问所以的属性的时候，都会访问这个方法，
    # 如果抛出一个普通的异常，如果你抛出的异常，刚好是 attribute
    # 这个方法，如果不明确的知道，如果定义了，最后一句，交给自己的父类处理，return 用自己的处理
    # 这种写法看上去对，实际上是不对的，递归 ，一直到底，大量的递归
    # 实例的所有属性方法，第一个都会调用__getattribute__这个方法
    # 如果自己定义了，就会覆盖父类的方法
    # 该方法
    # 要写一个代码
    # 要抛出一个 attribitre
    # 他的返回值将作为属性的查找
    # __getattribute__方法中为了避免在该方法中无限递归，它就应该永远的调用基类的同名方法以访问的任何属性，例如，object.__getattribute__
    # __getattr__() 当通过搜索实例，实例的类及祖先的类查不到属性，就会调用此方法
    # __setattr__() 通过访问实例属性，进行增加，进行增加，修改都要调用它
    # __getattribute__() ，实例的所有的属性调用都是从这个方法开始的
    #  属性的查找顺序 __getattribute__() --> instance.__dict__-->instance.__class__.__dict__-->继承祖先类(直到 object) -->
    #  调用__getattr__()
    #
    def __getattribute__(self, item): # item 是属性名，只要进行实例的属性访问，如果这里抛出异常，将不
        #return self.__dict__
        #pass
        #return 1000
        #raise AttributeError('89999999999')
        return object.__getattribute__(self,item)



p1 = Point(4,5)
print(1,p1.__dict__)
print(2,p1.xxxx )