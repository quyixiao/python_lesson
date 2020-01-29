# python 包管理
# 以便供人使用,目的也是为了复用
# distutils
# 官方库distutils,使用了安装用本setup.py来构建，安装包
# 从1998年就是标准库的一部分，直到2000年停止开发
# setuptools
# 它是替代distutils 的增强版工具集，包含easy_install工具，使用
# 提供了bdist_wheel 作为setuptools的扩展命令，这个命令可以用来生成新的打包格式wheel
# pip从1.4版本开始，提供了一个wheel子命令来安装wheel包，当然，需要先安装wheel 模块，
# 它可以让Python库以二进制形式安装，而不需要在本地安装
#