"""Python Sorting Practice - TODO
目标：练习基础排序与优化排序，不使用 Python 内置排序。
Goal: practice basic sorting methods and one optimized method without built-in sorting.
"""


# 题1：冒泡排序 Bubble Sort
# 中文：每一轮把当前最大的数“冒泡”到右边。
# English: On each pass, bubble the largest value to the right.
def bubble_sort(nums):
    arr = nums[:]
    i = 0
    n = len(arr)
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            j += 1
        i += 1
    return arr


# 题2：优化版冒泡排序 Optimized Bubble Sort
# 中文：如果某一轮没有发生交换，说明数组已经有序，可以提前结束。
# English: If no swap happens in one pass, the array is already sorted.
def bubble_sort_optimized(nums):
    arr = nums[:]
    i = 0
    n = len(arr)
    while i < n -1:
        swap = False
        j = 0
        while j< n - 1 - i:
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swap = True
            j += 1
        if not swap:
            break
        i += 1
    return arr


# 题3：选择排序 Selection Sort
# 中文：每一轮在未排序区间里找最小值，放到前面。
# English: On each pass, find the minimum in the unsorted part and place it in front.
def selection_sort(nums):
    arr = nums[:]
    i = 0
    min_inx = 0
    n = len(arr)
    while i < n:
        min_inx = i
        j = i + 1
        while j < n:
            if arr[j] < arr[min_inx]:
                min_inx = j
            j += 1
        arr[min_inx], arr[i] = arr[i], arr[min_inx]
        i += 1
    return arr


# 题4：插入排序 Insertion Sort
# 中文：把当前元素插入到前面已经有序的部分。
# English: Insert the current element into the correct position of the sorted prefix.
def insertion_sort(nums):
    arr = nums[:]
    i = 1
    n = len(arr)
    while i < n:
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        i += 1
    return arr


# 题5：归并排序 Merge Sort
# 中文：把数组不断拆分，再把两个有序部分合并。
# English: Split the array recursively, then merge sorted halves.
def merge_sort(nums):
    if len(nums) <= 1:
        return nums[:]
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    return result



if __name__ == '__main__':
    arr = [1, 4, 3, 9, 8, 7, 5, 6]
    print('1)', bubble_sort(arr))
    print('2)', bubble_sort_optimized(arr))
    print('3)', selection_sort(arr))
    print('4)', insertion_sort(arr))
    print('5)', merge_sort(arr))
