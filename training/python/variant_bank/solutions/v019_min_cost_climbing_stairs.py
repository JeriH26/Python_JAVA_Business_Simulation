"""V019 Min Cost Climbing Stairs
Time: O(n), Space: O(1)
"""


def solve(cost):
    prev2 = prev1 = 0
    for i in range(2, len(cost) + 1):
        prev2, prev1 = prev1, min(prev1 + cost[i - 1], prev2 + cost[i - 2])
    return prev1


if __name__ == '__main__':
    print(solve([10, 15, 20]))
