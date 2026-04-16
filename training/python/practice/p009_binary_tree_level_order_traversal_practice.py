"""P009 Binary Tree Level Order Traversal Practice
Algorithm: BFS using queue
TODO: implement solve(root)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        if level == len(result):
            result.append([])
        result[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(solve(root))  # expected: [[3], [9, 20], [15, 7]]
