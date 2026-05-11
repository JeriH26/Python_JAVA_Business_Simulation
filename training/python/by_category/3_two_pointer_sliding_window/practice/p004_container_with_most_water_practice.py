"""P004 Container With Most Water Practice
Algorithm: Two pointers (greedy shrink)
TODO: implement solve(height)
"""


def solve(height):

    #best = 0
   #
    #for i in range(len(height)):
    #    for j in range(i+1, len(height)):
    #        area = min(height[i], height[j]) * (j-i)
    #        best = max(best, area)
    #return best

    best = 0
    left = 0
    right = len(height) - 1
    while left < right:
        width = right - left
        area = min(height[left], height[right]) * width
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


    


if __name__ == '__main__':
    print(solve([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # expected: 49
