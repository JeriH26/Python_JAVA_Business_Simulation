"""V002 Count Pairs Equal to Target
Time: O(n), Space: O(n)
"""

from collections import defaultdict


def solve(nums, target):
    counts = defaultdict(int)
    pairs = 0
    for num in nums:
        pairs += counts[target - num]
        counts[num] += 1
    return pairs


if __name__ == '__main__':
    print(solve([1, 1, 2, 2, 3], 4))
