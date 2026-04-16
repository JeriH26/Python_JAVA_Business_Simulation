"""P008 Search Insert Position Practice
Algorithm: Binary search boundary
TODO: implement solve(nums, target)
"""


def solve(nums, target):
    #raise NotImplementedError("TODO: implement p008 search insert position")
    #t_list = []
    #for i in range(len(nums)):
    #    if nums[i] == target:
    #        return i
    #    else:
    #        t_list.append(nums[i])
    #t_list.append(target)
    #N_list = sorted(t_list)
    #for j in range(len(N_list)):
    #    if N_list[j] == target:
    #        return j
    #return -1

    #for i in range(len(nums)):
    #    if nums[i] >= target:
    #        return i
    #return len(nums)

    left, right = 0, len(nums) -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
           


if __name__ == '__main__':
    print(solve([1, 3, 5, 6], 5))  # expected: 2
    print(solve([1, 3, 5, 6], 2))  # expected: 1
