# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        work = head
        while work.next:
            if work.val == work.next.val:
                work.next = work.next.next
            else:
                work = work.next
        return head