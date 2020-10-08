# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, None
        if head:
            fast = head.next
        while fast and fast.next:
            if fast is slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        


    def hasCycle(self, head: ListNode) -> bool:
        helper = set()
        p = head
        while p:
            if p in helper:
                return True
            helper.add(p)
            p = p.next
        return False

            