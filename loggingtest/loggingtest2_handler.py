# asctime                   %(asctime)s
# created
#
# 调试的，日志系统很多，普通的文本文件
# 每一个Logger实例的level如同入口，让水流进来，如果这个门槛太高，信息就进不来，信息就进不来，例如
# log3.warnging('log3'),如果log3的级别太高，就不能进来
# Pass to handlers of current logger
# ls propagate true for current logger
# is there a parent logger
# Set current logger to parent
# Emit includes formatting
# Logger objects have a threefold job. First ,they expose several methods to application to
#

import logging
# 根logging 如果没有创建的话，
#
FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

log1 = logging.getLogger(__name__)
print(log1.name)
handler = logging.FileHandler('/Users/quyixiao/ttg/xxx','w')
log1.setLevel(10)
fmt = logging.Formatter(FORMAT)
handler.setFormatter(fmt)
log1.addHandler(handler)

log1.info('893298329328')

log1.debug('debuge')
log1.info("{}{}".format(1,'mageio8ie833333'))