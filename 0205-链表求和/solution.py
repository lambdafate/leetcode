# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        work = head
        flag = 0

        while l1 or l2:
            num = flag
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next

            flag = 1 if num >= 10 else 0
            num %= 10
            work.next = ListNode(num)
            work = work.next
        if flag == 1:
            work.next = ListNode(1)
        return head.next
