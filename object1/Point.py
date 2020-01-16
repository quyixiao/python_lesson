class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __repr__(self):
        return "__repr__<Point x={} ,y={}>".format(self.x ,self.y)

    def __hash__(self):
        return self.x + self.y

    def __eq__(self, other):
        return self.x + self.y == other.x + other.y

    def __str__(self):
        return "__str__<Point x={} ,y={}>".format(self.x, self.y)

print(hash(Point(4,5)))
1

lst = [Point(1,2),Point(3,4)]
print(lst)

dic = {Point(1,2),Point(1,2)}
print(dic)
