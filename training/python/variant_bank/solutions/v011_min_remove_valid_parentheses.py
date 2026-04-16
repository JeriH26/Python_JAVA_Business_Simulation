"""V011 Minimum Remove to Make Valid Parentheses
Time: O(n), Space: O(n)
"""


def solve(s):
    chars = list(s)
    stack = []

    for i, ch in enumerate(chars):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                chars[i] = ''

    for index in stack:
        chars[index] = ''

    return ''.join(chars)


if __name__ == '__main__':
    print(solve('a)b(c)d'))
