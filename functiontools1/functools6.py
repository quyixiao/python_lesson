cmds = {}

cmd = input('>>>')


# ls => ls()
# grep => grep()
#


def default_func():
    pass


def reg(cmd, fn):
    cmds[cmd] = fn


def mag():
    print('magedu')


def py():
    print('python')


reg('mag', mag)
reg(py, py)

while True:
    cmd = input('>>>').strip()
    if cmd == 'quit':
        break
    func = cmds.get(cmd, default_func)






