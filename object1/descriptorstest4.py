class Person:
    def __init__(self, name: str, age: int):
        print(name, age)
        params = ((name, str), (age, int))
        if not self.checkdata(params):
            raise TypeError('类型异常')
        self.name = name
        self.age = age

    def checkdata(self, params):
        for n, t in params:
            if not isinstance(n, t):
                print(n, '你传入的参数类型不正确', ',传入类型', type(n), '实际需要类型,', t, '参数类型不正确')
                return False
        return True


p1 = Person('tom', 20)
p2 = Person('jerry', '38')
