# asctime                   %(asctime)s
# created
#
# 调试的，日志系统很多，普通的文本文件
#
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0
# 2020-02-02 19:44:47.391 【INFO】 [Slf4jAgent.java:51]
# root
# s
# s.s1
# s.s1.s2

import logging

FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


log1 = logging.getLogger(__name__)
root = logging.Logger.root

log1.info(str(log1))
log1.info(str(log1.level))
print(root, root.level, id(log1.parent), id(root), root.parent)

print('11111111111111111', log1.getEffectiveLevel()) # 有效级别
log1.info('839283298')
log1.setLevel(logging.DEBUG)

print('22222222222222222', log1.getEffectiveLevel()) # 有效级别
log1.debug('8932222222222222')


log2 = logging.getLogger(__name__ + '.child')
print(log2.name,id(log2.parent),id(log1))
# 每一个logger创建后，都有一个等效的level
# logger对象可以在创建后动态的修改自己的level
# Handler 控制日志信息的输出目的地，可以是控制台，文件
# 可以单独的设置level
# 可以是单独的格式
# 可以设置过滤器
# handler 类继承
# Handler类继承，
# Handler
# StreamHandler 不指定使用sys.stderr
# FileHandler
print(log2.level,log2.getEffectiveLevel()) # level ,这个level，如果自己不设置，从自己的父亲那里来
#


