"""V030 Median from Data Stream
Time: O(log n) add, O(1) median, Space: O(n)
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2


if __name__ == '__main__':
    finder = MedianFinder()
    finder.add_num(1)
    finder.add_num(2)
    print(finder.find_median())
    finder.add_num(3)
    print(finder.find_median())
