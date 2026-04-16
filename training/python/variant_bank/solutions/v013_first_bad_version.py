"""V013 First Bad Version
Time: O(log n), Space: O(1)
"""


def solve(n, is_bad):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if is_bad(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    first_bad = 4
    print(solve(5, lambda version: version >= first_bad))
