# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(None, None)
        p, flag = ret, 0
        while l1 or l2:
            value = flag
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            value, flag = value % 10, value // 10
            p.next = ListNode(value)
            p = p.next
        if flag != 0:
            p.next = ListNode(flag, None)
        return ret.next
