"""P025 Evaluate Reverse Polish Notation Practice
Algorithm: stack for operands
TODO: implement solve(tokens)
"""


def solve(tokens):
    stack = []
    for t in tokens:
        if t in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[-1]


if __name__ == '__main__':
    print(solve(["2", "1", "+", "3", "*"]))  # expected: 9
    print(solve(["4", "13", "5", "/", "+"]))        # expected: 6
