# @functorls.lru_cache(maxsize=128,typed=False)
# Least-recently-used装饰器，lru,最近最少使用，cache 缓存
#  如果 maxsize 设置为 None，则要求用 LRU功能，并且缓存可以无限制增长，当 maxsize 是二的幂的时候，LRU功能执行得最好
# 如果 typed  设置为 True,则不同类型的函数参数，将单独缓存，例如 f(3) 和 f(3.0)将被视为具有不同结果的不同调用

