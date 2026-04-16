"""V029 Kth Smallest in Sorted Matrix
Time: O(n log(max-min)), Space: O(1)
"""


def solve(matrix, k):
    n = len(matrix)
    left, right = matrix[0][0], matrix[-1][-1]

    def count_less_equal(value):
        row = n - 1
        col = 0
        count = 0
        while row >= 0 and col < n:
            if matrix[row][col] <= value:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == '__main__':
    print(solve([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
