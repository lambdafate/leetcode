# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        helper = set()
        workA, workB = headA, headB
        while workA or workB:
            if workA is not None:
                if workA in helper:
                    return workA
                helper.add(workA)
                workA = workA.next
            if workB is not None:
                if workB in helper:
                    return workB
                helper.add(workB)
                workB = workB.next
        return None