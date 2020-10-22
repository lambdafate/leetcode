# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        if n <= 0:
            return head
        nhead = ListNode(None, head)
        work, tail = nhead, nhead
        for _ in range(n):
            if tail.next is None:
                return nhead.next
            tail = tail.next
        while tail.next:
            work = work.next
            tail = tail.next
        work.next = work.next.next
        return nhead.next