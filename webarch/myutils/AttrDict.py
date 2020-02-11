
class AttrDict:
    def __init__(self, d: dict):
        self.__dict__.update(d)

    def __setattr__(self, key, value):
        raise NotImplementedError()

    def __repr__(self):
        return "{}".format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)
