# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
        快慢指针法
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nhead = ListNode(None, head)
        left, right = nhead, nhead
        while n != 0:
            n, right = n-1, right.next
        while right.next:
            left, right = left.next, right.next
        next_node = left.next
        left.next = next_node.next
        return nhead.next

    
    """
        求链表长度法
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length, p = 0, head
        while p:
            length, p = length+1, p.next
        length = length - n
        nhead = ListNode(None, head)
        p = nhead
        while length != 0:
            length, p = length-1, p.next
        next_node = p.next
        p.next = next_node.next
        return nhead.next
