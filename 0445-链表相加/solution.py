# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getLinkNum(l1)
        num2 = self.getLinkNum(l2)
        sumNum = num1 + num2
        nhead = None
        while sumNum != 0:
            tmp = ListNode(sumNum % 10)
            sumNum = sumNum // 10
            tmp.next = nhead
            nhead = tmp
        if nhead is None:
            nhead = ListNode(0)
        return nhead
            
    def getLinkNum(self, head):
        p = head
        ret = 0
        while p:
            ret = ret * 10 + p.val
            p = p.next
        return ret
    
    
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseLink(l1)
        l2 = self.reverseLink(l2)
        flag = 0
        nhead = ListNode(None)
        tail = nhead
        while l1 or l2:
            tmp = flag
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            flag = tmp // 10
            tmp = tmp % 10
            tail.next = ListNode(tmp)
            tail = tail.next
        if flag == 1:
            tail.next = ListNode(1)
        ret = self.reverseLink(nhead.next)
        return ret
        
    def reverseLink(self, head):
        nhead = None
        p = head
        while p:
            tmp = p
            p = p.next
            tmp.next = nhead
            nhead = tmp
        return nhead
