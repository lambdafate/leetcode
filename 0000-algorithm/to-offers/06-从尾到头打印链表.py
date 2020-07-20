# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    def reversePrint(self, head: ListNode) -> List[int]:
        nhead = None
        while head:
            tmp = head
            head = head.next
            tmp.next = nhead
            nhead = tmp
        res = []
        while nhead:
            res.append(nhead.val)
            nhead = nhead.next
        return res
    """

    # use stack
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        i, j = 0, len(stack)-1
        while i < j:
            stack[i], stack[j] = stack[j], stack[i]
            i += 1
            j -= 1
        return stack
