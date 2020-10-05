# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        nhead = ListNode(None)
        nhead.next = head
        prev, work = nhead, nhead.next
        while work and work.next:
            if work.next.val != work.val:
                prev, work = work, work.next
                continue
            tmp = work.val
            while work and work.val == tmp:
                work = work.next
            prev.next = work
        return nhead.next