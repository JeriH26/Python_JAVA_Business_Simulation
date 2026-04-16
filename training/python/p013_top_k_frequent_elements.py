"""P013 Top K Frequent Elements
Time: O(n log k), Space: O(n)
"""

from collections import Counter
import heapq


def solve(nums, k):
    freq = Counter(nums)
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for _, num in heap]


if __name__ == '__main__':
    print(solve([1, 1, 1, 2, 2, 3], 2))
