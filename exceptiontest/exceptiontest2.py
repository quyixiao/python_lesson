# 最终一定要执行，如果没有执行的话，就一定要执行
# 有异常
class MyExctionError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

try:
    print('-----------------------')
    #raise MyExctionError('Wrong', '4040')
    print('============')
except  LookupError as e:
    print('catch', 'lookup', e.args)
except MyExctionError as  e:
    print('catch', 'MyExctionError', e.code, e.message)
except Exception('Exception')  as e:
    print('Exception')
finally:
    print('finally ')