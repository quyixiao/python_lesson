#  格式定义如下
#  class 子类名中（基类1 [,基类2,....]）
#  如果类的定义，没有基类的列表，等同埋于继承自 object,在 python3 中
# 面向对象三要素，继承 Inheritance
# 人类和猫继承了父母的一部分特征，但是可以有自己的个性
# 在面向对象世界中，从父类继承，就可以直接拥有父类的属性和方法，这样可以减少代码，多复用，子类可以定义自己的属性方法
# 看一个不用继承的例子
# 继承是面向对象的重要的特点，python 内存模型和 java 和 C++是完全不一样的，字典
# Animal 就是 cat 的父类，也称为基类，超类，
# 子类，
# Cat 是 animal 的子类，也称为派生类，
# 多继承，也是尽量的少继承，
# 如果类定义时，没有基类列表，等同于继承自object，在 python3 中，object 类是所有对象的根基类
# 属性查找顺序，实例__dict__>类__dict__如果有继承==>父类的__dict__
#  描述器
# 不管怎样说，属性的查找方式，是不可变的,函数
# 

class Animal:
    def shout(self):
        print(self.__class__.__name__ + " to shut ")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

cat = Cat()
cat.shout()


dog = Dog()
dog.shout()



print(Dog.mro())
print(Dog.__mro__)
