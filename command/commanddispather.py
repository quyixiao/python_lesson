# 完善命令分发器 ，实现函数可以带带任意参数（可变参数除外），解析参数并要求用户输入
# 思路
# 可以注册的时候，固定死@reg('py',200,1000)
# 可以认为@reg('py',200,100)和@reg('py',300,100)是不同的函数，可以用 partial 函数
# 进行时，在输入 cmd 的时候，逗号分割，获取参数
# 至于函数的验证，以后实现
# 一般用户都喜欢使用单纯的一个命令如 mag , 然后直接显示想要的结果，所以采用第一种方式

from functools import partial


# 自定义函数可以直接任意参数，可变参数，keyword-only 除外
def command_dispatcher():
    # 构建全局字典
    cmd_tab1 = {}

    # 注册函数
    def reg(cmd, *args, **kwargs):
        def _reg(fn):
            func = partial(fn, *args, **kwargs)
            cmd_tab1[cmd] = func
            return func

        return _reg

    def default_fun():
        print('Unknown command')

    # 调试器
    def dispatcher():
        while True:
            cmd = input("please input cmd >> ")
            # 提出条件
            if cmd.strip() == '':
                return
            cmd_tab1.get(cmd, default_fun)()

    return reg, dispatcher


reg, dispatcher = command_dispatcher()


# 自定义函数
@reg('mag', z=200, y=300, x=100)
def foo1(x, y, z):
    print('magedu', x, y, z)


@reg('py', 300, b=400)
def foo2(a, b=1000):
    print('python', a, b)


# 调度循环
dispatcher()
