# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        nhead = ListNode(None, head)
        info = {}
        work = head
        while work:
            if work.val not in info:
                info[work.val] = True
            else:
                info[work.val] = False
            work = work.next
        work = nhead
        while work.next:
            if not info[work.next.val]:
                work.next = work.next.next
            else:
                work = work.next
        return nhead.next