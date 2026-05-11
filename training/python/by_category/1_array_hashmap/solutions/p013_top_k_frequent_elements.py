"""P013 Top K Frequent Elements
Brute-force-ish readable version:
1) Count each number frequency
2) Sort by frequency descending
3) Take first k

Time: O(n log n), Space: O(n)
"""

import heapq


def solve(nums, k):
    # Step 1: count frequency manually (no Counter)
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: convert to list of (num, count)
    pairs = []
    for num, count in freq.items():
        pairs.append((num, count))

    # Step 3: sort by count descending
    pairs.sort(key=lambda x: x[1], reverse=True)

    # Step 4: take first k numbers
    ans = []
    i = 0
    while i < k and i < len(pairs):
        ans.append(pairs[i][0])
        i += 1

    return ans


def solve_heap(nums, k):
    """Optimized version using a size-k min-heap.

    Time: O(n log k), Space: O(n)
    """
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for _, num in heap]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print('simple_sort:', solve(nums, k))
    print('min_heap   :', solve_heap(nums, k))
