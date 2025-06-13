from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    previous = None
    current = head

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous
