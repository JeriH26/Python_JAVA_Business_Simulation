"""P024 Daily Temperatures Practice
Algorithm: monotonic decreasing stack of indices
TODO: implement solve(temperatures)
"""


def solve(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
           j = stack.pop()
           ans[j] = i - j
        
        stack.append(i)
    
    return ans


if __name__ == '__main__':
    print(solve([73, 74, 75, 71, 69, 72, 76, 73]))  # expected: [1,1,4,2,1,1,0,0]
