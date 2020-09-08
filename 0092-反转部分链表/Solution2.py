# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        nhead = ListNode(None, head)
        prev = nhead
        for _ in range(m-1):
            prev = prev.next
        p = prev.next
        for _ in range(n-m):
            next_node = p.next
            p.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        return nhead.next

