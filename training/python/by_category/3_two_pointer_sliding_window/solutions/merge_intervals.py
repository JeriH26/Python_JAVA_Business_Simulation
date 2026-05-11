"""Merge Intervals (LeetCode 56)
Time: O(n log n), Space: O(n)
"""

def merge(intervals):
    if not intervals:
        return []
    intervals.sort()  # 按起点排序
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # 有重叠
            merged[-1][1] = max(merged[-1][1], end)  # 扩展终点
        else:
            merged.append([start, end])  # 新区间
    return merged

if __name__ == '__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # expected: [[1,6],[8,10],[15,18]]
    print(merge([[1,4],[4,5]]))                # expected: [[1,5]]
