# 很尴尬中会生成大量的系统日志，应用程序日志安全日志等日志，通过对日志的分析可以了解服务器的负载，
# 一般采集的流程是
# 日志产出，采集，存储分析，存储（数据库,NOSQL）-> 可视化
#  日志产出，采集（logstash,Flume,Scribe）->存储，分析-存储（ 数据库，NoSql）-> 可视化
# 日志告诉你，一行
# 缺点：
#  数据并没有很好的分割，比如时间就被分开了，URL也被分割了，User Agent 空格最多，分割了
# 所以，定义的时候不选用这种在 field 中出现的字符 就可以省很多事，例如使用


# 16533953143  172.16.11.8
# 16533953051  172.16.11.7
# 以日志中的时间为准
# 看时间是否符合 width ,在其中
#

