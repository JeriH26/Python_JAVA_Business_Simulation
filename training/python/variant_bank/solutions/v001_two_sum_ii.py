"""V001 Two Sum II (Sorted Array)
Time: O(n), Space: O(1)
"""


def solve(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []


if __name__ == '__main__':
    print(solve([2, 7, 11, 15], 9))
