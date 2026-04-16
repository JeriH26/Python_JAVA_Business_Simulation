"""V025 K Closest Points to Origin
Time: O(n log k), Space: O(k)
"""

import heapq


def solve(points, k):
    heap = []
    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(heap, (-dist, [x, y]))
        if len(heap) > k:
            heapq.heappop(heap)
    return [point for _, point in heap]


if __name__ == '__main__':
    print(solve([[1, 3], [-2, 2]], 1))
