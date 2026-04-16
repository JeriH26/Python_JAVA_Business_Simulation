"""V024 Non-overlapping Intervals
Time: O(n log n), Space: O(1) extra
"""


def solve(intervals):
    intervals.sort(key=lambda interval: interval[1])
    removed = 0
    end = float('-inf')

    for start, finish in intervals:
        if start < end:
            removed += 1
        else:
            end = finish

    return removed


if __name__ == '__main__':
    print(solve([[1, 2], [2, 3], [3, 4], [1, 3]]))
