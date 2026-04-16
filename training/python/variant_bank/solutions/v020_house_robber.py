"""V020 House Robber
Time: O(n), Space: O(1)
"""


def solve(nums):
    take = skip = 0
    for num in nums:
        take, skip = skip + num, max(skip, take)
    return max(take, skip)


if __name__ == '__main__':
    print(solve([2, 7, 9, 3, 1]))
