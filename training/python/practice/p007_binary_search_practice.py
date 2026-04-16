"""P007 Binary Search Practice
Algorithm: Binary search on sorted array
TODO: implement solve(nums, target)
"""


def solve(nums, target):
    #raise NotImplementedError("TODO: implement p007 binary search")

    #for i in range(len(nums)):
    #    if nums[i] == target:
    #        return i
    #return -1

    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left += 1
        else:
            right -= 1
    return -1
    
    
        

if __name__ == '__main__':
    print(solve([-1, 0, 3, 5, 9, 12], 9))  # expected: 4
    print(solve([-1, 0, 3, 5, 9, 12], 2))  # expected: -1
