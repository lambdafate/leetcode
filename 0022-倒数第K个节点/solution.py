# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        nhead = ListNode(None)
        nhead.next = head
        tail = nhead
        for _ in range(k):
            if tail is None:
                return None
            tail = tail.next
        while tail:
            tail = tail.next
            nhead = nhead.next
        return nhead