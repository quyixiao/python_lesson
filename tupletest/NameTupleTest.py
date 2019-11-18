from collections import namedtuple

Point = namedtuple('P', ['x', 'y'])
print(Point)

p1 = Point(10, 20)
print(p1)

print(p1.x, p1.y)

print(p1[0], p1[1])


Student = namedtuple('stu','name age')
s1 = Student('tom',20)
s2 = Student('jerry',30)
print(s1.name)
print(s2.age)

