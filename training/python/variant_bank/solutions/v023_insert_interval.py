"""V023 Insert Interval
Time: O(n), Space: O(n)
"""


def solve(intervals, new_interval):
    ans = []
    i = 0

    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        ans.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    ans.append(new_interval)
    ans.extend(intervals[i:])
    return ans


if __name__ == '__main__':
    print(solve([[1, 3], [6, 9]], [2, 5]))
