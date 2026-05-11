"""While Loop Practice - 练习版
每一题只用 while 循环完成，不允许用 for。
做完每题对照 while_loop_solutions.py 的答案。
"""


# 题1：打印 1 到 n
# 输入：n=5  输出：1 2 3 4 5
def print_1_to_n(n):
    i = 1
    while i <= n:
        print(i, end="")
        i += 1
    print()


# 题2：数组求和
# 输入：[1, 2, 3, 4]  输出：10
def array_sum(nums):
    i = 0
    summ = 0
    while i < len(nums):
        summ += nums[i]
        i += 1
    return summ


# 题3：找数组最大值
# 输入：[3, 1, 4, 1, 5, 9]  输出：9
def find_max(nums):
    i = 0
    maxx = 0
    while i < len(nums):
        maxx = max(maxx, nums[i])
        i += 1
    return maxx


# 题4：反转字符串
# 输入："hello"  输出："olleh"
def reverse_string(s):
    n = len(s)
    i = n - 1
    result = ""
    while i >= 0:
        result = result + s[i]
        i -= 1
    return result


# 题5：左补零对齐
# 输入：s="9", n=3  输出："009"
def pad_zeros(s, n):
    while len(s) < n:
        s = "0" + s
    return s


# 题6：双指针判断回文
# 输入："racecar"  输出：True
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -=1
    return True


# 题7：二分搜索
# 在已排序数组里找 target，返回下标，找不到返回 -1
# binary_search([1,3,5,7,9], 5)
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (right - left) // 2
        if nums[mid] == target:
            return mid
        left += 1
    return -1


# 题8：滑动窗口 - 同向双指针
# 找没有重复字符的最长子串长度
# 输入："abcabcbb"  输出：3
def longest_unique_substring(s):
    left = 0
    right = 0
    seen = {}
    max_len = 0

    while right < len(s):
        ch = s[right]
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        max_len = max(max_len, right - left + 1)
        right += 1

    return max_len


# 题9：链表遍历
# 遍历链表，把所有节点的值加入列表并返回
# 建链表 1->2->3
# head = ListNode(1, ListNode(2, ListNode(3)))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_array(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next

    return result


# 题10：BFS 队列遍历
# 层序遍历二叉树，返回每层的值列表
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_level_order(root):
    return root


if __name__ == '__main__':
    print("题1:", end=" "); print_1_to_n(5)
    print("题2:", array_sum([1, 2, 3, 4]))
    print("题3:", find_max([3, 1, 4, 1, 5, 9]))
    print("题4:", reverse_string("hello"))
    print("题5:", pad_zeros("9", 3))
    print("题6:", is_palindrome("racecar"))
    print("题7:", binary_search([1,3,5,7,9], 5))
    print("题8:", longest_unique_substring("abcabcbb"))
    head = ListNode(1, ListNode(2, ListNode(3)))
    print("题9:", linked_list_to_array(head))
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print("题10:", bfs_level_order(root))
