"""P017 Reverse Linked List Practice
Algorithm: Iterative — track prev/curr pointers
TODO: implement solve(head)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    raise NotImplementedError("TODO: implement p017 reverse linked list")


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
