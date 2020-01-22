
print(__name__)

class A:
    def getmodule(self):
        print(self.__module__.__name__)



print(__name__,A().getmodule())














