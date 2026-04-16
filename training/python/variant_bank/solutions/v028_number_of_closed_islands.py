"""V028 Number of Closed Islands
Time: O(m * n), Space: O(m * n)
"""


def solve(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if grid[r][c] == 1 or (r, c) in visited:
            return True

        visited.add((r, c))
        up = dfs(r - 1, c)
        down = dfs(r + 1, c)
        left = dfs(r, c - 1)
        right = dfs(r, c + 1)
        return up and down and left and right

    closed = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and (r, c) not in visited and dfs(r, c):
                closed += 1
    return closed


if __name__ == '__main__':
    sample = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
    print(solve(sample))
