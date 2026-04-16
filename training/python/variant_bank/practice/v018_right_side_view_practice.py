"""V018 Binary Tree Right Side View Practice
TODO: implement solve(root)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):
    raise NotImplementedError("TODO: implement v018 right side view")


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(4))
    print(solve(root))  # expected: [1, 3, 4]
