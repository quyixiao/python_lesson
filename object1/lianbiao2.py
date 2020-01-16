#
import bisect

origin = [37, 99, 73, 48, 47, 39, 41, 25, 99, 51]
sorted_list = sorted(origin)
nums = [20, 40, 42, 100, 210, 5]
print(list(enumerate(sorted_list)))


#
# def bi_insert_sort(origin, num):
#     low = 0
#     high = len(origin)
#
#     ret = origin[:]
#     while low < high:
#         mid = (low + high) // 2
#         if num < ret[mid]:  # 向左 中点是
#             high = mid - 1
#         else:  # >= 向右
#             low = mid + 1
#     return low
# for x in nums:
#     sorted_list.insert(bi_insert_sort(sorted_list,x),x)

# print(sorted_list)
# for x in nums:
#     index = bisect.bisect(sorted_list, x)
#     sorted_list.insert(index , x)
#
# print(sorted_list)


for x in nums:
    bisect.insort(sorted_list,x)

print(sorted_list) #[5, 20, 25, 37, 39, 40, 41, 42, 47, 48, 51, 73, 99, 99, 100, 210]