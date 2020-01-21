# 最终一定要执行，如果没有执行的话，就一定要执行
# 有异常

f = None
try:
    f = open('test.log')
except Exception('Exception')  as e:
    print('Exception')
finally:
    if f :
        f.closed
    print('finally ')