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


dispatcher();
