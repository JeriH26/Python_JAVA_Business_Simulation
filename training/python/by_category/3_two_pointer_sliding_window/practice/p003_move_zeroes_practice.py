"""P003 Move Zeroes Practice
Algorithm: Two pointers (in-place overwrite)
TODO: implement solve(nums)
"""


def solve(nums):
    
    #read = 0
    #write = 0
    #while read < len(nums):
    #    if nums[read] != 0:
    #        nums[write], nums[read] = nums[read], nums[write]
    #        write += 1
    #    read += 1
    #return nums

    i = 0
    for j in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            i += 1
    return nums


if __name__ == '__main__':
    print(solve([3, 1, 0, 3,0, 12]))  # expected: [1, 3, 12, 0, 0]
    print(solve([0, 0, 1]))
