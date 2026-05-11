"""P023 Min Stack (LeetCode 155)
Design a stack supporting push, pop, top, and get_min in O(1).
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


def solve(ops):
    """Execute operations list like [("push", -2), ("get_min",), ...]."""
    ms = MinStack()
    out = []
    for op in ops:
        if op[0] == "push":
            ms.push(op[1])
            out.append(None)
        elif op[0] == "pop":
            out.append(ms.pop())
        elif op[0] == "top":
            out.append(ms.top())
        elif op[0] == "get_min":
            out.append(ms.get_min())
    return out


if __name__ == '__main__':
    operations = [("push", -2), ("push", 0), ("push", -3), ("get_min",), ("pop",), ("top",), ("get_min",)]
    print(solve(operations))  # expected: [None, None, None, -3, -3, 0, -2]
