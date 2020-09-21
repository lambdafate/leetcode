# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        nhead = ListNode(None, head)
        prev, curr = nhead, head
        while curr and curr.next:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = curr
            prev.next = next_node
            prev = curr
            curr = curr.next
        return nhead.next


