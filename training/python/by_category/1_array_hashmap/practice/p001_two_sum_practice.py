"""P001 Two Sum Practice
Algorithm: Hash map (one-pass lookup)
TODO: implement solve(nums, target)
"""


def solve(nums, target):
    #n = len(nums)
    #for i in range(n):
    #    for j in range(i+1, n):
    #        if nums[i] + nums[j] == target:
    #            return [i, j]
    #return []

    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []

    



if __name__ == '__main__':
    print(solve([2, 11, 7, 15, 7], 9))  # expected: [0, 2]
