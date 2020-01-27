# 异常
# raise  激活异常，正在出炉的异常，
# 我们要异常，不是我们想象中的异常，以为拿到我们的异常，通过这种使用，我们不太建义，
# 一般，return null
# 我们在先不考虑异常，如果异常不考虑的话，主线程最简单的东西是记住的，如何产生异常
#
import sys

def mathtest():
    try:
        # raise A ()
        # raise 1 # exceptions must derive from BaseException 异常必须由baseException 类来抛出
        print('1111111')
        # raise  # 如果这样写，将出现没有被激活的异常 No active exception to reraise
        # raise IndentationError('我要异常')
        # ret  = 1 / 0  # (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x1076ed410>)


    except Exception as e:  # 处理的异常# # ，
        print(e)
        print('exc')
        print(sys.exc_info())
        # raise # RuntimeError: No active exception to reraise
    else:
        print('else ')
    finally:
        print('finally')


mathtest()