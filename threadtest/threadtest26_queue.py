import datetime
import logging
import random
import threading
import time

from threading import BoundedSemaphore, Semaphore
from queue import Queue


# GIL全局解释器锁
# CPython在解释器进程级别有一把锁，叫做GIL全局解释器锁
# GIL保证CPython进程中，只有一个进程执行字节码，甚至是多核CPU的情况下，也是只能允许一个CPU上的一个线程在运行
# CPython中
# IO密集型，由于线程阻塞，就会调用其他的线程
# CPU密集型，当前线程可能会连续的获取GIL,导致其他的线程几乎无法使用CPU
# 在CPython中由于有GIL存在，IO密集型，使用多线程较为合算，CPU密集型，使用了多线程，要绕开GIL
# 新版Cpython正在努力的优化GIL的问题，但不是移除
# 如果在意多线程的效率问题，请绕行，选择其它的语言erlang,Go等
# Python中绝大多数内置数据结构的读，写操作都是原子操作
# 由于GIL的存在，Python的内置数据类型在多线程编程的时候就变成安全的了，但是实际上它们本身不是线程安全类型
# 保留GIL的原因：
#       Guido坚持简单的哲学，对于初学者门槛低，不需要高深的系统知识也能安全，简单的使用Python
# 而且移除GIL,会降低CPython单线程的执行效率
# 测试下面的2个程序，请问下面的程序是计算密集型还是IO密集型
#

FORMAT = '%(asctime)-15s \t [%(threadName)s ,%(thread)8d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)











