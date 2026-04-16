"""V021 3Sum Closest
Time: O(n^2), Space: O(1)
"""


def solve(nums, target):
    nums.sort()
    best = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(best - target):
                best = total
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total

    return best


if __name__ == '__main__':
    print(solve([-1, 2, 1, -4], 1))
