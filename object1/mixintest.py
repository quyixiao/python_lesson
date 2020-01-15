# Minxin 本质上是多继承的  实现
# mixin 体现的是一种组合的设计模式
# 在面向对象的设计中，一个复杂的类往往需要很多的功能，而这些功能有的来自于不同的类提供，这就需要很多的组合在一起
# 从设计角度来说，多组合，少继承
# Mixin 类的使用原则
# Mixin 类中不就方显示的出现__init__初始化方法
# Mixin 通常不能独立的工作，因为它是准备混入别的类的功能实现
# Mixin 类通常在继承列表中的第一个位置，例如 class PrintableWord (PringableMixin,Word):pass
# Mixin 类和装饰器
# 这两种方式都可以使用，看个人喜好
# 如果不需要就继承就是使用 Mixin 类的方式
# 达到我的目的都是好方法，
# 后面，会讲
# 练习


class Document:
    def __init__(self, content):
        self.content = content

    def print(self):
        raise NotImplementedError('抽象基类没有实现')


class Word(Document):
    def print(self):
        print('我要实现')


class Pdf(Document):
    def print(self):
        print('pdf pdf ')


def printable(cls):
    cls.print = lambda self: print(self.content)
    return cls


@printable
class PrintableWord(Word):
    pass


word = Word('test word')
word.print()

p = PrintableWord('89432222222222')
p.print()


class Printable:
    def print(self):
        print(self.content)


class PrintableWord(Printable, Pdf):
    pass


ppdf = PrintableWord("tesio");
ppdf.print()

