"""P021 Contains Duplicate (LeetCode 217)
Time: O(n), Space: O(n)
"""


def solve(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == '__main__':
    print(solve([1, 2, 3, 1]))  # expected: True
    print(solve([1, 2, 3, 4]))  # expected: False
