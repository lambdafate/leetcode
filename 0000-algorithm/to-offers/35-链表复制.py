# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        work, nhead = head, Node(0)
        p = nhead
        nodes, helper, index = [], {}, 0
        while work:
            helper[work] = index
            index, work = index+1, work.next
        work = head
        while work:
            p.next = Node(work.val, None, None)
            # record random index
            p.next.random_index = helper[work.random] if work.random else -1
            p, work = p.next, work.next
            nodes.append(p)
        work = nhead.next
        while work:
            if work.random_index != -1:
                work.random = nodes[work.random_index]
            work = work.next
        return nhead.next
