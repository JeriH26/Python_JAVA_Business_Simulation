"""V017 Binary Tree Zigzag Level Order Practice
TODO: implement solve(root)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):
    raise NotImplementedError("TODO: implement v017 zigzag level order")


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(solve(root))  # expected: [[3], [20, 9], [15, 7]]
