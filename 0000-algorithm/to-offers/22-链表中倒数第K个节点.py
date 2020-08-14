# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        nhead = ListNode(0)
        nhead.next = head
        work, tail = nhead, head
        for _ in range(k):
            if tail is None:
                return head
            tail = tail.next
        while tail is not None:
            work = work.next
            tail = tail.next
        return work.next
