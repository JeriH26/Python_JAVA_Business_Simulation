"""V006 Stable Sort by Parity
Time: O(n), Space: O(n)
"""


def solve(nums):
    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 != 0]
    return evens + odds


if __name__ == '__main__':
    print(solve([3, 1, 2, 4]))
