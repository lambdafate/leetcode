# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        nhead = ListNode(0)
        nhead.next = head
        work = nhead
        while work.next is not None:
            tmp = work.next
            # find it
            if tmp.val == val:
                work.next = tmp.next
                break
            work = work.next
        return nhead.next