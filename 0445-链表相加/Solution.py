# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.convertNumber(l1)
        num2 = self.convertNumber(l2)
        value = num1 + num2
        if value == 0:
            return ListNode(0)
        head = None
        while value:
            v, value = value % 10, value // 10
            tmp = ListNode(v, head)
            head = tmp
        return head    
    def convertNumber(self, head):
        num, p = 0, head
        while p:
            num = num * 10 + p.val
            p = p.next
        return num