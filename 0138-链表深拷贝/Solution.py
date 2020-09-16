# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        nhead = Node(0)
        work = nhead
        info = {}
        while head:
            tmp = Node(head.val, None, head.random)
            info[head] = tmp
            work.next = tmp
            work = work.next
            head = head.next
        work = nhead.next
        while work:
            if work.random is not None:
                work.random = info[work.random]
            work = work.next
        return nhead.next
