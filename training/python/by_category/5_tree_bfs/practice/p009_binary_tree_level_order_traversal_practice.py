"""P009 Binary Tree Level Order Traversal Practice
Algorithm: BFS using queue
TODO: implement solve(root)
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
    
    ans = []
    q = deque([root])
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    
    return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(solve(root))  # expected: [[3], [9, 20], [15, 7]]
