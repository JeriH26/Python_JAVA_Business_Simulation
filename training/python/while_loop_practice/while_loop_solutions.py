"""While Loop Practice
从简单到复杂，每题只用 while 循环完成，不允许用 for。
"""


# ─────────────────────────────────────────
# 题1：打印 1 到 n
# 输入：n=5  输出：1 2 3 4 5
# ─────────────────────────────────────────
def print_1_to_n(n):
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1
    print()


# ─────────────────────────────────────────
# 题2：数组求和
# 输入：[1, 2, 3, 4]  输出：10
# ─────────────────────────────────────────
def array_sum(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total


# ─────────────────────────────────────────
# 题3：找数组最大值
# 输入：[3, 1, 4, 1, 5, 9]  输出：9
# ─────────────────────────────────────────
def find_max(nums):
    max_val = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_val:
            max_val = nums[i]
        i += 1
    return max_val


# ─────────────────────────────────────────
# 题4：反转字符串
# 输入："hello"  输出："olleh"
# ─────────────────────────────────────────
def reverse_string(s):
    result = ""
    i = len(s) - 1
    while i >= 0:
        result = result + s[i]
        i -= 1
    return result


# ─────────────────────────────────────────
# 题5：左补零对齐（p019 的核心！）
# 输入：s="9", n=3  输出："009"
# ─────────────────────────────────────────
def pad_zeros(s, n):
    while len(s) < n:
        s = "0" + s
    return s


# ─────────────────────────────────────────
# 题6：双指针判断回文（p028 的核心！）
# 输入："racecar"  输出：True
# ─────────────────────────────────────────
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# ─────────────────────────────────────────
# 题7：二分搜索（p007 的核心！）
# 在已排序数组里找 target，返回下标，找不到返回 -1
# ─────────────────────────────────────────
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ─────────────────────────────────────────
# 题8：滑动窗口 - 同向双指针（p005 的核心！）
# 找没有重复字符的最长子串长度
# 输入："abcabcbb"  输出：3
# ─────────────────────────────────────────
def longest_unique_substring(s):
    # seen 记录窗口内的字符
    seen = {}
    left = 0
    max_len = 0

    right = 0
    while right < len(s):
        ch = s[right]

        # 如果 ch 已在窗口里，收缩左边直到它被移出
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        max_len = max(max_len, right - left + 1)
        right += 1

    return max_len


# ─────────────────────────────────────────
# 题9：链表遍历（p017/p018 的核心！）
# 遍历链表，把所有节点的值加入列表并返回
# 建链表 1->2->3
# head = ListNode(1, ListNode(2, ListNode(3)))
# ─────────────────────────────────────────
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_array(head):
    result = []
    curr = head          # curr 从 head 出发
    while curr:          # curr 不为 None 就继续
        result.append(curr.val)
        curr = curr.next  # 移到下一个节点
    return result


# ─────────────────────────────────────────
# 题10：BFS 队列遍历（p009/p014 的核心！）
# 层序遍历二叉树，返回每层的值列表
# ─────────────────────────────────────────
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_level_order(root):
    if not root:
        return []

    queue = [root]   # 队列：存“还没处理”的节点，初始先放根节点
    result = []

    while queue:              # 队列不空就继续（还有节点等着处理）
        size = len(queue)     # 当前层有多少个节点（这一轮只处理这 size 个）
        level = []
        i = 0
        while i < size:
            node = queue.pop(0)     # 从队头取出一个“当前要处理”的节点
            level.append(node.val)  # 记录当前节点值

            # 把下一层节点加入队尾，保证后续按 FIFO（先进先出）处理
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            i += 1

        # 当前层处理完，加入结果
        result.append(level)

    return result


if __name__ == '__main__':
    print("题1:", end=" "); print_1_to_n(5)        # 1 2 3 4 5
    print("题2:", array_sum([1, 2, 3, 4]))         # 10
    print("题3:", find_max([3, 1, 4, 1, 5, 9]))    # 9
    print("题4:", reverse_string("hello"))         # olleh
    print("题5:", pad_zeros("9", 3))               # 009
    print("题6:", is_palindrome("racecar"))        # True
    print("题6:", is_palindrome("hello"))          # False
    print("题7:", binary_search([1,3,5,7,9], 5))  # 2
    print("题7:", binary_search([1,3,5,7,9], 4))  # -1
    print("题8:", longest_unique_substring("abcabcbb"))  # 3
    # 建链表 1->2->3
    head = ListNode(1, ListNode(2, ListNode(3)))
    print("题9:", linked_list_to_array(head))      # [1, 2, 3]
    # 建树     1
    #         / \
    #        2   3
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print("题10:", bfs_level_order(root))          # [[1], [2, 3]]
