"""P015 Kth Largest Element in an Array
Time: O(n log k), Space: O(k)
"""

import heapq


def solve(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == '__main__':
    print(solve([3, 2, 1, 5, 6, 4], 2))
