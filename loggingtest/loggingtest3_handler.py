# asctime                   %(asctime)s
# created
#
#

import logging
# 根logging 如果没有创建的话，
#
FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

log1 = logging.getLogger('log1main')
log1.setLevel(0)

handler = logging.FileHandler('/Users/quyixiao/ttg/xxx','w')
log1.addHandler(handler)
log1.info('log1 hello')
log1.debug('debug')
log1.warning('warning')


