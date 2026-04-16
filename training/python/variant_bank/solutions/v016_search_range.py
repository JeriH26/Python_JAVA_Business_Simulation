"""V016 Search Range
Time: O(log n), Space: O(1)
"""

import bisect


def solve(nums, target):
    left = bisect.bisect_left(nums, target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = bisect.bisect_right(nums, target) - 1
    return [left, right]


if __name__ == '__main__':
    print(solve([5, 7, 7, 8, 8, 10], 8))
