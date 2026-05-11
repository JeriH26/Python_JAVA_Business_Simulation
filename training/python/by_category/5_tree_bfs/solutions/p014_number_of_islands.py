"""P014 Number of Islands
Time: O(m * n), Space: O(m * n)
"""

from collections import deque


def solve(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited.add((sr, sc))

        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                bfs(r, c)

    return islands


if __name__ == '__main__':
    sample = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    print(solve(sample))
