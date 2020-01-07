# 有一个配置文件，内容如下，

import configparser
import json

src = 'test.ini'
dst = 'test.json'

cfg = configparser.ConfigParser()
cfg.read(src)

d = {}  # 嵌套机构，来自于cfg 内部字典

for k, v in cfg.items():
    print(k)
    print(k, cfg.items(k))
    d[k] = dict(cfg.items(k))

print(d)

#

#
with open(dst, 'w+') as f:
    json.dump(d,f)
