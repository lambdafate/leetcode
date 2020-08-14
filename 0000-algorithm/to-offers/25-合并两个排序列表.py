# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        work = res
        while l1 is not None and l2 is not None:
            tmp = l2
            if l1.val <= l2.val:
                tmp = l1
                l1 = l1.next
            else:
                l2 = l2.next
            work.next = tmp
            work = work.next
        work.next = l2 if l1 is None else l1
        return res.next
            
