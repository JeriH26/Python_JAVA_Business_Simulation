"""P012 Merge Intervals
Time: O(n log n), Space: O(n)
"""


def solve(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]

    for start, end in intervals[1:]:
        last = merged[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])

    return merged


if __name__ == '__main__':
    print(solve([[1, 3], [2, 6], [8, 10], [15, 18]]))
