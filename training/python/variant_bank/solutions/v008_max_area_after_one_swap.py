"""V008 Max Area After One Swap
Time: O(n^4) worst-case for small training inputs, Space: O(n)
"""


def _container_area(height):
    best = 0
    left, right = 0, len(height) - 1
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return best


def solve(height):
    best = _container_area(height)
    nums = height[:]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            best = max(best, _container_area(nums))
            nums[i], nums[j] = nums[j], nums[i]
    return best


if __name__ == '__main__':
    print(solve([1, 2, 4, 3]))
