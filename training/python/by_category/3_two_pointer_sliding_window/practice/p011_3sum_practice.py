"""P011 3Sum Practice
Algorithm: Sorting + two pointers
TODO: implement solve(nums)
"""


def solve(nums):

#    n = len(nums)
#    ans = []
#    seen = set()
#    for i in range(n):
#        for j in range(i+1, n):
#            for k in range(j+1, n):
#                if nums[i] + nums[j] + nums[k] == 0:
#                    triplet = sorted([nums[i], nums[j], nums[k]])
#                    triplet = tuple(triplet)
#                
#                    if triplet not in seen:
#                        seen.add(triplet)
#                        ans.append(list(triplet))
#    
#    return ans

    nums.sort()
    ans = []
    n = len(nums)

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return ans

if __name__ == '__main__':
    print(solve([-1, 0, 1, 2, -1, -4]))  # expected: [[-1, -1, 2], [-1, 0, 1]]
