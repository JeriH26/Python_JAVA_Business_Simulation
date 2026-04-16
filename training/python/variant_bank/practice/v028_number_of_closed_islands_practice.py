"""V028 Number of Closed Islands Practice
TODO: implement solve(grid)
"""


def solve(grid):
    raise NotImplementedError("TODO: implement v028 number of closed islands")


if __name__ == '__main__':
    sample = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
    print(solve(sample))  # expected: 2
