"""V012 Remove Outermost Parentheses
Time: O(n), Space: O(n)
"""


def solve(s):
    depth = 0
    parts = []
    for ch in s:
        if ch == '(':
            if depth > 0:
                parts.append(ch)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                parts.append(ch)
    return ''.join(parts)


if __name__ == '__main__':
    print(solve('(()())(())'))
