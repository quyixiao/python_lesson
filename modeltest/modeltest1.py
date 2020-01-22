import sys
import re
import os
# from 后面必须是模块 import 后面可能是类，函数，方法
#
#from os.path import join as j,exists as ex,split
# import 模块1[,模块2,...] 完全导入
# import .. as .. 模块别名
# import 语句
# 总结，导入顶级模块，其名称会加入到本地名词空间中，并绑定到其模块对象
# 导入非顶级模块，只需要将其顶级模块名称加入到本地名词空间中，导入模块必须使用完全的媛宝名称来访问
# 如果使用了as,as 后名称直接绑定到导入的模块对象中，
# from pathlib import Path * 在当前名词空间导入公有的或者非下划线开头的，或者指定成员
# 总结 ： 找到from子句中指定的模块，加载并初始化它（注意不是导入）
# 对于import 子句后面的名称
#   先查from子句导入模块是否具有该名称的属性
#   如果不是，则尝试导入该名称的子模块
#   还没有找到，则抛出ImportError 异常
#   这个名称保存到本地名字空间中，如果有as子句，则使用as子句后的名称
#

print(dir())

print(__file__)
print(__name__)

print(sys.__name__)
print(__package__)
print(111111111,__spec__)

if __name__ == '__main__':
    print('main')


