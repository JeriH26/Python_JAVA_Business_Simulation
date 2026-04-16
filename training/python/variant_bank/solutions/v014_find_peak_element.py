"""V014 Find Peak Element
Time: O(log n), Space: O(1)
"""


def solve(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    print(solve([1, 2, 3, 1]))
