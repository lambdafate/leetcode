# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        length = self.linkLength(head)
        ret = self.recursion(head, length, k)
        return ret

    def recursion(self, head, length, k):
        if length < k:
            return head
        nhead = None
        work = head
        for _ in range(k):
            tmp = work
            work = work.next
            tmp.next = nhead
            nhead = tmp
        head.next = self.recursion(work, length-k, k)
        return nhead

    def linkLength(self, head):
        ret = 0
        while head:
            ret += 1
            head = head.next
        return ret