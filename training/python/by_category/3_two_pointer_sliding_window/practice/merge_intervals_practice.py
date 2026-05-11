"""Merge Intervals (LeetCode 56)
Time: O(n log n), Space: O(n)
"""

def merge(intervals):

    if not intervals:
        return[]
    
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if result[-1][1] >= start:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result


if __name__ == '__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # expected: [[1,6],[8,10],[15,18]]
    print(merge([[1,4],[4,5]]))                # expected: [[1,5]]
