# 类定义，实体和类之间对应
# 元类是制造类的工厂，是生成类的类
# 定义一个元类，需要使用type(name,bases,dict,)也可以继承type
# 构造好的元类，就可以在类定义是使用关键字参数metaclass指定元类，可以使用最原始的metatype(name,bases,dict)的方式的构造一个类
# 元类__new__() 方法中，可以获得元类信息，当前类，基类，类属性的字典
# 元编程一般用户构架开发 中
# 开发中，除非你明确的知道你自己要做什么，否则不需要随便的使用元编程
# 99%的情况下，用不到元类，可能有一些程序员一辈子也用不到元编程
# Django,SQLAlchemy使用了元类，让我们使用起来非常的方便
#
class Field:  # 字段类
    def __init__(self, fieldname=None, pk=False, nullable=True):
        self.fieldname = fieldname
        self.pk = pk
        self.nullable = nullable


class ModelMeta(type):  # 元类
    def __new__(cls, name, bases, attrs: dict):
        print('------------------------------')
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        print('--------------__tablename__--------------', name)
        #hasattr(cls,'__tablename__') ???? 这个是错误的，因为cls
        if '__tablename__' not in attrs.keys():
            attrs['__tablename__'] = name
        primary_keys = []

        for k, v in attrs.items():
            if isinstance(v, Field):
                if v.pk:
                    print('1111111111111111', k, v)
                    primary_keys.append(v)

        attrs['__pks__'] = primary_keys

        return super().__new__(cls, name, bases, attrs)


class Base(metaclass=ModelMeta):
    """它自己和子类来自于"""
    pass


print('=' * 30)


class Student(Base):
    id = Field(pk=True)
    name = Field('username', nullable=False)
    age = Field()
