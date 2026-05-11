"""P027 Minimum Depth of Binary Tree (LeetCode 111)
Time: O(n), Space: O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):
    if not root:
        return 0

    q = deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solve(root))  # expected: 2
