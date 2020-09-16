# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        list1, list2 = [], []
        work = head
        while work:
            if work.val < x:
                list1.append(work.val)
            else:
                list2.append(work.val)
            work = work.next
        list1.extend(list2)
        work = head
        for val in list1:
            work.val = val
            work = work.next
        return head
        