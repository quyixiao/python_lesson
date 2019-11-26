num_list = [[1, 9, 8, 5, 6, 7, 4, 3, 2],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]]
nums = num_list[1]
print(nums)
length = len(nums)
count_swap = 0
count = 1
for i in range(length):
    for j in range(length - i - 1):
        count += 1
        if nums[j] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
            count_swap += 1

print(nums, count_swap, count)
