from distutils.core import setup
import glob

#
# setup(name='m',
#       version='1.0.1',
#       description='oweiieow',
#       author='quyixiao',
#       author_email='2621048238@qq.com',
#       url='http://www.baidu.com',
#       packages=['argparse1'],
#       )


setup(name='m', # name 名字
      version='1.0.1', # version 版本信息
      description='oweiieow', # 描述信息
      author='quyixiao', #
      author_email='2621048238@qq.com',
      url='http://www.baidu.com',
      packages=['webarch'],  # 将非目录子包加入进来
      data_file=glob.glob('webarch/templates/*.html')  # 加入模版
      )
