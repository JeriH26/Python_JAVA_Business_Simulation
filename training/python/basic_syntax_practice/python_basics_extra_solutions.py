"""Python Basics Extra Practice - Solutions"""


# 题1：区分输入是 None、空值还是非空值。
# 思路：先判断是否为 None，再判断是否为空字符串/空列表/空字典。
# print('1)', classify_input(None))               # none
# print('1)', classify_input(''))                 # empty
# print('1)', classify_input([1]))                # non-empty
def classify_input(x):
    """Distinguish None from empty containers/strings and non-empty values."""
    if x is None:
        return "none"
    if x == "" or x == [] or x == {}:
        return "empty"
    return "non-empty"


# 题2：演示返回值约定。
# 约定：nums 为 None 返回 None；空列表返回 -1；否则返回第一个元素。
# print('2)', first_element_or_default(None))     # None
# print('2)', first_element_or_default([]))       # -1
# print('2)', first_element_or_default([9, 8]))   # 9
def first_element_or_default(nums):
    """Demonstrate explicit return contracts for None/empty/non-empty."""
    if nums is None:
        return None
    if len(nums) == 0:
        return -1
    return nums[0]


# 题3：找到目标值最后一次出现的位置。
# 思路：从左到右扫描，命中 target 就更新 last，最后返回 last。
# print('3)', find_last_index([1,2,3,2], 2))     # 3
# print('3)', find_last_index([1,2,3], 9))       # -1
def find_last_index(nums, target):
    """Scan all elements and keep updating last seen index."""
    last = -1
    i = 0
    while i < len(nums):
        if nums[i] == target:
            last = i
        i += 1
    return last


# 题4：统计闭区间 [left, right] 对应的元素数量。
# 边界：left > right 时直接返回 0。
# print('4)', count_inclusive([10,20,30,40], 1, 2))  # 2
# print('4)', count_inclusive([10,20,30,40], 3, 1))  # 0
def count_inclusive(nums, left, right):
    """Handle off-by-one correctly for inclusive boundaries [left, right]."""
    if left > right:
        return 0

    count = 0
    i = left
    while i <= right and i < len(nums):
        count += 1
        i += 1
    return count


# 题5：Two Sum 返回值约定版。
# 约定：找到一对下标返回 [i, j]；找不到返回 []。
# print('5)', two_sum_contract([2,7,11,15], 9))      # [0,1]
# print('5)', two_sum_contract([1,2,3], 100))        # []
def two_sum_contract(nums, target):
    """Return [] when no valid pair exists."""
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1
    return []


# 题6：查找目标值下标。
# 约定：存在返回下标；不存在返回 -1。
# print('6)', find_index_contract([5,6,7], 6))       # 1
# print('6)', find_index_contract([5,6,7], 9))       # -1
def find_index_contract(nums, target):
    """Return -1 when target is absent."""
    i = 0
    while i < len(nums):
        if nums[i] == target:
            return i
        i += 1
    return -1


# 题7：max 的手写 fallback。
# 思路：先把第一个元素作为当前最大值，再逐个比较更新。
# print('7)', max_fallback([3,9,1]))                 # 9
# print('7)', max_fallback([]))                      # None
def max_fallback(nums):
    """Manual fallback for max(nums)."""
    if len(nums) == 0:
        return None

    best = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > best:
            best = nums[i]
        i += 1
    return best


# 题8：sorted 的手写 fallback（选择排序）。
# 思路：每一轮在未排序区域找最小值，放到当前位置。
# print('8)', sort_fallback([3,1,2]))                # [1,2,3]
def sort_fallback(nums):
    """Manual fallback for sorted(nums) using selection sort."""
    arr = nums[:]
    i = 0
    while i < len(arr):
        min_idx = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        i += 1
    return arr


if __name__ == '__main__':
    print('1)', classify_input(None))               # none
    print('1)', classify_input(''))                 # empty
    print('1)', classify_input([1]))                # non-empty

    print('2)', first_element_or_default(None))     # None
    print('2)', first_element_or_default([]))       # -1
    print('2)', first_element_or_default([9, 8]))   # 9

    print('3)', find_last_index([1,2,3,2], 2))     # 3
    print('3)', find_last_index([1,2,3], 9))       # -1

    print('4)', count_inclusive([10,20,30,40], 1, 2))  # 2
    print('4)', count_inclusive([10,20,30,40], 3, 1))  # 0

    print('5)', two_sum_contract([2,7,11,15], 9))      # [0,1]
    print('5)', two_sum_contract([1,2,3], 100))        # []

    print('6)', find_index_contract([5,6,7], 6))       # 1
    print('6)', find_index_contract([5,6,7], 9))       # -1

    print('7)', max_fallback([3,9,1]))                 # 9
    print('7)', max_fallback([]))                      # None

    print('8)', sort_fallback([3,1,2]))                # [1,2,3]
