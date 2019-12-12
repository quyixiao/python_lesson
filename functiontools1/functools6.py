cmds = {}

# ls => ls()
# grep => grep()
#
def reg(c):
    def _reg(fn):
        cmds[c] = fn
        return fn
    return _reg



def dispatcher():
    def default_func():
        print('未知命令')

    while True:
        cmd = input('>>>').strip()
        if cmd == 'quit':
            break
        cmds.get(cmd, default_func)()

@reg('mag')
def mag():
    print('magedu')

@reg('py')
def py():
    print('python')

@reg('ls')
def ls():
    print('ls')


#reg('mag', mag)
# reg('py', py)
# reg('ls', ls)


dispatcher()












