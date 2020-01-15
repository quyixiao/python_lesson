class Temperature:
    def __init__(self,t,unit='c'):
        self._c = None
        self._f = None
        self._k = None
        if unit == 'f':
            pass
        elif unit == 'k':
            pass
        else :
            self._c = t

    @classmethod
    def c2f (cls):
        pass


    def c2f (self):
        pass

    def c2c (self):
        pass

    @staticmethod
    def c2k():
        pass
