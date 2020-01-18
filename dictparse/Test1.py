import random

print([print('{}*{} = {:<3}{}'.format(j, i, i * j, '\n' if i == j else ''), end=" ") for i in range(1, 10) for j in
       range(1, i + 1)]
      )
#


# 生成 ID
# '0089.irtfyxmwjq' 是 id的格式，要求 id 的格式以点号为分割，左边是4位，从1 开始整数，右边是10位随机小写英文字母，请依次生成
# 10个 id 的列表
# 我觉得这个东西是个好的东西是的，但是还是不是太好，所以，我觉得就不要这样的子了
# 哈哈，是不是
#

#
import string

print(
    [
        print('{:0>4d}.{}'.format(i, "".join(random.sample(string.ascii_lowercase, 10))), end='\n')
        for i in range(1, 101)
    ]
)

print('=========================================')

print(
    [
        print('{:04}.{}'.format(i, "".join(random.sample([chr(i) for i in range(97, 123)], 10))), end='\n')
        for i in range(1, 101)
    ]
)

# 上面也是一个很轻巧的实现

print(
    [
        '{:04}.{}'.format(n, ''.join([random.choice(bytes(range(97, 123)).decode()) for _ in range(10)]))
        for n in range(1, 101)
    ]
)
#
print(
    ["{:04}.{}".format(i, "".join([chr(random.randint(97, 122)) for j in range(10)]))
     for i in range(1, 101)]
)
print(
    [
        '{:>04}.{}'.format(i, ''.join(random.choice(string.ascii_lowercase) for _ in range(0, 10)))
        for i in range(1, 101)
    ]
)
