# ls => ls()
# grep => grep()
#

def cmd_dispatcher():
    cmds = {}

    def reg(c):
        def _reg(fn):
            cmds[c] = fn
            return fn

        return _reg

    def disp():
        def default_func():
            print('未知命令')

        while True:
            cmd = input('>>>').strip()
            if cmd == 'quit':
                break
            cmds.get(cmd, default_func)()

    return reg, disp


reg, dispatcher = cmd_dispatcher()


@reg('mag')
def mag():
    print('magedu')


@reg('py')
def py():
    print('python')


@reg('ls')
def ls():
    print('ls')


dispatcher()



#  实现一个 cache装饰器，实现可过期的清除功能
# 简化设计，函数的形参定义不包含可变位置参数，可变关键字词参数和 keyword-only 参数
# 可以不考虑缓存满了换出问题
# 写一个命令分发器
#  如果一个函数使用同样的 cmd 名称注册，就等于覆盖œœ