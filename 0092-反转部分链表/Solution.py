# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        nhead = Node(0)
        nhead.next = head
        prev = nhead
        for _ in range(m-1):
            prev = prev.next

        begin = prev.next
        for _ in range(n-m):
            tmp = begin.next
            begin.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        return nhead.next
