"""Python Basics Extra Practice - TODO
Focus:
1) None vs truthy/falsy checks
2) Off-by-one boundaries
3) Return value contracts
4) Built-in fallback implementations
"""


# 1) None / empty checks
# Return one of: "none", "empty", "non-empty"
# print('1)', classify_input(None))               # none
# print('1)', classify_input(''))                 # empty
# print('1)', classify_input([1]))                # non-empty
def classify_input(x):
    if x == None:
        return "none"
    if x == '':
        return "empty"
    return "non-empty"


# 2) Safe first element
# If nums is None -> return None
# If nums is []   -> return -1
# Else return first element
# print('2)', first_element_or_default(None))     # None
# print('2)', first_element_or_default([]))       # -1
# print('2)', first_element_or_default([9, 8]))   # 9
def first_element_or_default(nums):
    if nums == None:
        return None
    if nums == []:
        return -1
    return nums[0]


# 3) Boundary: find last index of target (linear scan)
# Return -1 if not found
# print('3)', find_last_index([1,2,3,2], 2))     # 3
# print('3)', find_last_index([1,2,3], 9))       # -1
def find_last_index(nums, target):
    last = -1
    i = 0
    while i < len(nums):
        if nums[i] == target:
            last = i
        i += 1
    return last


# 4) Boundary: count elements in inclusive range [left, right]
# If left > right, return 0
# print('4)', count_inclusive([10,20,30,40], 1, 2))  # 2
# print('4)', count_inclusive([10,20,30,40], 3, 1))  # 0
def count_inclusive(nums, left, right):
    count = 0
    if left > right:
        return 0
    
    i = left
    while i <= right and i < len(nums):
        count += 1
        i += 1
    return count


# 5) Return contract: two sum index pair
# Return [] if no solution
# print('5)', two_sum_contract([2,7,11,15], 9))      # [0,1]
# print('5)', two_sum_contract([1,2,3], 100))        # []
def two_sum_contract(nums, target):
    seen = {}
    i = 0
    while i < len(nums):
        need = target - nums[i]
        if need in seen:
            return [seen[need], i]
        seen[nums[i]] = i
        i += 1
    return []


# 6) Return contract: find target index
# Return -1 if not found
# print('6)', find_index_contract([5,6,7], 6))       # 1
# print('6)', find_index_contract([5,6,7], 9))       # -1
def find_index_contract(nums, target):
    #for i in range(len(nums)):
    #    if nums[i] == target:
    #        return 1
    i = 0
    while i < len(nums):
        if nums[i] == target:
            return 1
        i += 1
    return -1


# 7) Fallback for max(nums) without built-in max
# Return None if nums is empty
# print('7)', max_fallback([3,9,1]))                 # 9
# print('7)', max_fallback([]))                      # None
def max_fallback(nums):
    if nums == []:
        return None
    i = 0
    max_num = nums[0]
    while i < len(nums):
        if nums[i] > max_num:
            max_num = nums[i]
        i += 1
    return max_num


# 8) Fallback for sorted(nums) ascending without built-in sorted
# Use simple selection sort and return a NEW list
# print('8)', sort_fallback([3,1,2]))                # [1,2,3]
def sort_fallback(nums):
    #arr = nums[:]
    #i = 0
    #n = len(arr)
    #while i < n - 1:
    #    j = 0
    #    while j < n - 1 - i:
    #        if arr[j] > arr[j+1]:
    #            arr[j+1], arr[j] = arr[j], arr[j+1]
    #        j += 1
    #    i += 1

    #arr = nums[:]
    #i = 0
    #n = len(arr)
    #while i < n:
    #    min_inx = i
    #    j = i + 1
    #    while j < n:
    #        if arr[j] < arr[min_inx]:
    #            min_inx = j
    #        j += 1
    #    arr[min_inx], arr[i] = arr[i], arr[min_inx]
    #    
    #    i += 1

    arr = nums[:]
    i = 1
    n = len(arr)
    while i < n:
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
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

    print('7)', max_fallback([11,9,1,10,7]))                 # 9
    print('7)', max_fallback([]))                      # None

    print('8)', sort_fallback([3,1,2]))                # [1,2,3]
