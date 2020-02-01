import importlib
# 上面的例子中的就是插件化编程的核心代码
# 依赖的技术，
# 反射，运行时获取类型信息，可以动态维护类型数据
# 动态的import ，推荐使用importlib模块，实现动态import功能
# 多线程，可以开启一个线程，等待用户输入，从而加载我绑定名称的模块
# 加载时机
# 什么时候加载合适
# 程序启动的时候，还是程序运行的时候中？
# 加载的时机
# 什么时候加载合适
# 程序启动时
# 像pycharm这样的工具，需要很多的组件 ，这些组件可能是插件，启动的时候扫的固定的目录，加载插件
# 程序运行中
# 在程序运行的过程中，接受用户指令或请求，启动相应的插件
# 程序运行中，
# 程序运行过程中，接受用户的指令或者请求，启动相应的插件
# 两种方式各有利弊，如果用记需要时加载，如果插件太多或者依赖多插件也会启动慢
# 所以先加载必须的，常用的插件，其他的插件使用时，发现需要动态加入
# 软件的设计不可能尽善尽美，或者在某些功能上，不可能做到专业，需要专业的客户自己增强
# 比如Photoshop的滤镜插件
# Nodepad++ ，它只需要做一个文本编辑器就可以了，其它的功能通过插件的方式提供
# 拼写检查，HTML预览，正则插件等
# 插件和接口的区别
# 接口往往是暴露出来的功能，例如模块提供的函数或方法，加载模块后调用这些函数，
# 如果大家完成里面的东西，这样的话，还是有一些好处的，专业，定制，想要什么版本，方便定制
# 自由的卖钱的，其他的插件加入，
# 如果一个软件，运行起来效率更加的高，插件化，想实现的话，就要想到很多的方法
# 动态加载这一个模块，插件，接口规范，就是这些东西，接口规范，
# 

def plugin(name: str, sep='.'):
    m, _, c = name.partition(sep)
    # mod = __import__(mode_name)
    mod = importlib.import_module(m)
    print(mod)
    cls = getattr(mod, c)
    return cls


if __name__ == '__main__':
    mod = plugin('t2.A')
    a = mod()
    a.show()
    print(locals())