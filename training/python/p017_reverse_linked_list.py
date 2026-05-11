"""P017 Reverse Linked List (LeetCode 206)
Time: O(n), Space: O(1)

Given the head of a singly linked list, reverse the list and return the reversed list.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


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
    head = make_list([1, 2, 3, 4, 5])
    print(to_list(solve(head)))  # expected: [5, 4, 3, 2, 1]

    head2 = make_list([1, 2])
    print(to_list(solve(head2)))  # expected: [2, 1]

    print(to_list(solve(None)))   # expected: []
