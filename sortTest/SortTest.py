# 依次接收用户输入的3个数 ，排序后打印
# 1.转换int后，判断大小的排序，使用分支结构完成
# 2.使用max函数
# 3.使用列表的sort方法
# 冒泡法
nums = []

for i in range(3):
    nums.append(int(input('{}:'.format(i))))

nums.sort(reverse=True)
print(nums)
