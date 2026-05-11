"""P026 Binary Tree Right Side View (LeetCode 199)
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
        return []

    q = deque([root])
    ans = []

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == size - 1:
                ans.append(node.val)

    return ans


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(solve(root))  # expected: [1, 3, 4]
