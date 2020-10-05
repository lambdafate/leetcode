# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        length = self.linkLength(head)
        if length < k:
            return head
        nhead, p = None, head
        for _ in range(k):
            tmp = p
            p = p.next
            tmp.next = nhead
            nhead = tmp
        head.next = self.reverseKGroup(p, k)
        return nhead
        
    def linkLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
