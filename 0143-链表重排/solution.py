# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        nhead = ListNode(None, head)
        slow, fast = nhead, nhead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        work0 = head
        work1 = self.reverseLink(slow.next)
        slow.next = None
        while work0 and work1:
            tmp = work1
            work1 = work1.next
            tmp.next = work0.next
            work0.next = tmp
            work0 = tmp.next
        return nhead.next

    def reverseLink(self, head):
        nhead = None
        while head:
            tmp = head
            head = head.next
            tmp.next = nhead
            nhead = tmp
        return nhead