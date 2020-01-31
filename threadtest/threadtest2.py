import threading
import time  # 线程对象


# current_thread()      返回当前线程对象
# main_thread()         返回主线程对象
# active_count()        当前牌alive状态的线程个数
# enumerate()           返回所有活着的线程列表，不包括已经终止的线程和未开始的线程
# get_ident()           返回当前线程ID,非0整数
# active_count,enumerate 方法返回的值还包括主线程
# Thread实例的属性和方法
# 名称
# name ,只是一个名字，只是一个标识，名称可以重名，getName()，setName()获取，设置这个名词
# ident 线程id,它是一个非0整数，线程启动后才会有ID,否则为None,线程退出，此Id依旧可以访问，此id可以重复使用
# is_alive() ，返回线程是否活着
# 注意，线程的name这是一个名称，可以重复，ID 必须唯一，但是可以线程退出后再利用
# 在同一时间之内去看，线程的id是不可以重复的，线程的名字是可以重复的
# 

def add(x, y):
    print(getthreadinfo() + '--------------------' + ' ' + str(x) + ' ' + str(y) + '---------' + str(x + y))
    return x + y


def getthreadinfo():
    return (str(threading.current_thread().ident) + ' ' + threading.current_thread().name + ' ' +
            threading.main_thread().name + ' ' + str(threading.active_count()) + ' '
            + str(threading.enumerate()) + ' ' + str(threading.get_ident()))


print('111111111111111')
t = threading.Thread(target=add, args=(4, 5),name='th1')  # 创建新的线程
t1 = threading.Thread(target=add, args=(4,), kwargs={'y': 6},name='th2')  #
t2 = threading.Thread(target=add, kwargs={'x': 4, 'y': 7},name='th3')  #
ts = []
ts.append(t)
ts.append(t1)
ts.append(t2)




if __name__ == '__main__':
    print('3333333333333333333333')
    # t.start()
    # t1.start()
    # t2.start()

    ts[0].start()
    time.sleep(10)
    print('++++++++++++++++++++++++')
    if ts[0].is_alive():
        print('alive')
    else :
        print('deae')
        print(ts[0])
        ts[0].start()
