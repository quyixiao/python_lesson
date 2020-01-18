# 上例中使用了 getattr 方法找到对象的属性的方式，比自己维护一个字典来建立名称和函数之间的关系就好了
# 反射相关的魔术方法
# __getattr__(),__setattr__(),__delattr__()
#
class Dispatcher:
    def __init__(self):
        pass

    def reg(self, name, fn):
        setattr(self, name, fn)

    def ls(self):
        pass

    def run(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'quit':
                break
            getattr(self, cmd, lambda: print('Unknown Cmd {}'.format(cmd)))()


dis = Dispatcher()
dis.reg('ls', lambda: print('ls'))
dis.run()
