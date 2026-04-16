"""V005 Remove Element In Place
Time: O(n), Space: O(1)
"""


def solve(nums, val):
    write = 0
    for num in nums:
        if num != val:
            nums[write] = num
            write += 1
    return write


if __name__ == '__main__':
    sample = [3, 2, 2, 3]
    k = solve(sample, 3)
    print(k, sample[:k])
