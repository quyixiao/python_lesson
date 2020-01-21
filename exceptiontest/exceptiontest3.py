# 最终一定要执行，如果没有执行的话，就一定要执行
# 有异常
# 错误 Error
# 逻辑错误，算法写错了，加法写成了减法
# 笔误，变量名写错了，语法错误
# 函数或者类使用错误，其实这也属于逻辑错误
# 总之，错误可以避免的
# 异常 Exception
# 本章就是意外的情况
#

f = None
try:
    f = open('test.log')
except Exception('Exception')  as e:
    print('Exception')
finally:
    try:
        if f:
            f.close()
    except:
        pass

    print('finally ')
