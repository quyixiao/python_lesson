import argparse

parser = argparse.ArgumentParser(prog='ls', description='列出目录名称', add_help=True)
print(parser.prog)
parser.add_argument('path', nargs='?',default='.')
parser.add_argument('-l', action='store_true')
parser.add_argument('-a', '-all', action='store_true')
print('')
parser.print_help()
print('--------------------------------')
args = parser.parse_args('/etc -la'.split())
print(1, args, type(args))
print('++++++++++++++++++++++++++++++++++++++++++++++=')

# print(2, args.path, '--------------------', args.path1)
# 解析器的参数
# 参数名称      说明
# prog 程序的名字，缺省的是使用sys.argv[0]
# add_help 实现
# 位置参数的解析
# 运行的结果
# args = parser.parse_args() #分析参数
# parser.help() 是打印帮助
# args 参数列表，一个可迭代的对象，内部会氢可迭代的对象转换成list ，如果为None则使用命令行传入参数，非None
# Namespace(path='/etc')里面的path参数存储在一个Namespace对象的内的属性上
# nargs.add_argument('path',)