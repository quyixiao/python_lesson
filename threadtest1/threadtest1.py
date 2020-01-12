import threading


def add(x,y):
    ret = x + y # 开辟一个线程
    print(ret)
    return ret

t = threading.Thread(target=add ,args=(4,5)) # 线程对象的创建
t.start()