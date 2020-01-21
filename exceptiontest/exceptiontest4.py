import sys
import traceback


def foo2():
    try:
        a = 1 / 0
    except KeyError:
        pass


try:
    foo2()
except :
    print('error')
    print(sys.exc_info())
    traceback.print_tb(sys.exc_info()[2])
