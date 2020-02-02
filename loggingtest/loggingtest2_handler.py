# asctime                   %(asctime)s
# created
#
# 调试的，日志系统很多，普通的文本文件


import logging
# 根logging 如果没有创建的话，
#
FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

log1 = logging.getLogger(__name__)
print(log1.name)
handler = logging.FileHandler('/Users/quyixiao/ttg/xxx','w')

fmt = logging.Formatter(FORMAT)
handler.setFormatter(fmt)
log1.addHandler(handler)
log1.info('893298329328')

log1.debug('debuge')
log1.info("{}{}".format(1,'mageio8ie833333'))