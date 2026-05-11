"""Python Sorting Practice - Solutions

中文：排序专项，包含基础三种排序和一个 O(n log n) 优化解法。
English: Sorting practice including three basic sorts and one O(n log n) optimized method.
"""


# 题1：冒泡排序 Bubble Sort
# 中文：每一轮比较相邻两个元素，如果顺序错了就交换。
# English: Compare adjacent elements and swap when they are out of order.
def bubble_sort(nums):
    """Basic bubble sort, time O(n^2), space O(1) extra if in-place."""
    arr = nums[:]
    n = len(arr)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
    return arr


# 题2：优化版冒泡排序 Optimized Bubble Sort
# 中文：如果一整轮都没有交换，说明数组已经有序，可以提前结束。
# English: Stop early if a full pass makes no swaps.
def bubble_sort_optimized(nums):
    """Bubble sort with early-stop optimization."""
    arr = nums[:]
    n = len(arr)
    i = 0
    while i < n - 1:
        swapped = False
        j = 0
        while j < n - 1 - i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            j += 1
        if not swapped:
            break
        i += 1
    return arr


# 题3：选择排序 Selection Sort
# 中文：每一轮找到最小值的位置，然后和当前位置交换。
# English: Find the minimum index in the unsorted region and swap it forward.
def selection_sort(nums):
    """Selection sort, time O(n^2)."""
    arr = nums[:]
    n = len(arr)
    i = 0
    while i < n:
        min_idx = i
        j = i + 1
        while j < n:
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        i += 1
    return arr


# 题4：插入排序 Insertion Sort
# 中文：把当前位置元素拿出来，向左寻找正确插入位置。
# English: Take the current element and shift larger elements right until insertion point.
def insertion_sort(nums):
    """Insertion sort, good for small or nearly-sorted arrays."""
    arr = nums[:]
    n = len(arr)
    i = 1
    while i < n:
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        i += 1
    return arr


# 题5：归并排序 Merge Sort
# 中文：这是优化版标准解，时间复杂度稳定是 O(n log n)。
# English: This is the optimized standard solution with stable O(n log n) time.
def merge_sort(nums):
    """Merge sort, time O(n log n), extra space O(n)."""
    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


# 中文：合并两个已经排好序的数组。
# English: Merge two sorted arrays into one sorted array.
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
