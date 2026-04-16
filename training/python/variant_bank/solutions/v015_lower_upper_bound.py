"""V015 Lower Bound and Upper Bound
Time: O(log n), Space: O(1)
"""

import bisect


def solve(nums, target):
    first_ge = bisect.bisect_left(nums, target)
    first_gt = bisect.bisect_right(nums, target)
    return (first_ge, first_gt)


if __name__ == '__main__':
    print(solve([1, 2, 2, 2, 4], 2))
