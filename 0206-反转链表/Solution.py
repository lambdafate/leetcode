# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """ 
        递归反转
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        nhead = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return nhead




    """
        迭代反转
    """
    def reverseList(self, head: ListNode) -> ListNode:
        nhead, p = None, head
        while p:
            tmp, p = p, p.next
            tmp.next = nhead
            nhead = tmp
        return nhead
        
