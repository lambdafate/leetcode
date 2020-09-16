# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        nhead = ListNode(None, head)
        work = nhead
        used = set()
        while work.next:
            if work.next.val in used:
                work.next = work.next.next
            else:
                used.add(work.next.val)
                work = work.next
        return nhead.next