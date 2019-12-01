#datetime 模块
# 对日期，时间，时间来处理
# datetime 类
# 类方法
# today() 返回的是本地时间的 datetime  对象
# now(tz=None)  返回的当前时间的 datetime对象，时间为微秒，如果 tz 为 None，返回和 today() 一样
# utcnow() 一样
# fromtimestamp(timestamp,tz=None) 从一个时间
# datetime 对象
# timestamp()返回的是微秒的问题
# 时间
# 格林威治天文台1970 和 1月1 号点到现在的时间
#
import datetime

print(type(datetime.datetime.now()))
print(datetime.datetime(2017,10,1))


print(datetime.datetime.fromtimestamp(1))


b = datetime.datetime.now().weekday()
print(b )


b = 463


print('======================================')

g = ("{:4}".format(i) for i in range(1,11))
# 总结
# 延迟计算
# 返回迭代器，可以迭代
# 从前到后走完一遍后，不能回头
#
next(g)
print('+++++++++++++++++++++++++++++++')
for x in g :
    print(x)
print('----------------------')
for x in g :
    print(x)



