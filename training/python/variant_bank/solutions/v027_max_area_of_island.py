"""V027 Max Area of Island
Time: O(m * n), Space: O(m * n)
"""


def solve(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (
            r < 0 or r >= rows or c < 0 or c >= cols or
            grid[r][c] == 0 or (r, c) in visited
        ):
            return 0
        visited.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    best = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                best = max(best, dfs(r, c))
    return best


if __name__ == '__main__':
    print(solve([[0, 0, 1], [1, 1, 1], [0, 1, 0]]))
