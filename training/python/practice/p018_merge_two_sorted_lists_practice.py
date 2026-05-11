"""P018 Merge Two Sorted Lists Practice
Algorithm: Dummy node + two-pointer merge
TODO: implement solve(l1, l2)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(l1, l2):
    raise NotImplementedError("TODO: implement p018 merge two sorted lists")


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
