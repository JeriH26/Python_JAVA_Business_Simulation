"""P018 Merge Two Sorted Lists (LeetCode 21)
Time: O(m + n), Space: O(1)

Merge two sorted linked lists and return the merged list (sorted).

Example:
    Input:  l1 = 1 -> 2 -> 4,  l2 = 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


# --- helpers for testing ---
def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == '__main__':
    l1 = make_list([1, 2, 4])
    l2 = make_list([1, 3, 4])
    print(to_list(solve(l1, l2)))  # expected: [1, 1, 2, 3, 4, 4]

    print(to_list(solve(None, make_list([0]))))  # expected: [0]
    print(to_list(solve(None, None)))             # expected: []
