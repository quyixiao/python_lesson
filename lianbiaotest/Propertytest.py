class Property:
    def __init__(self, fget, fset=None):
        print('_Property___init__',fget,fset)
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        print('Property__get__',instance,owner)
        if instance is not None:
            return self.fget(instance)
        return self

    def __set__(self, instance, value):
        print('Property__set__',self,instance,value)
        self.fset(instance,value)

    def setter(self, fn):
        print('Property_setter', self,fn)
        self.fset = fn
        return self


class A:
    def __init__(self, data):
        print('A___init__',data)
        self._data = data

    @Property  # data 类属性，data = Property(data)
    def data(self):  # data 等价是什么，data = method
        print('A_Property_data')
        return self._data

    @data.setter
    def data(self, value):  # data 等价什么？ data = proj.setter(data)
        print('A_data.setter_',value)
        self._data = value


a = A(100)
print(a.data)
a.data = 200
print(a.data)
