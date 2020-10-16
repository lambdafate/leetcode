# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        分而治之
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        nhead = ListNode(None)
        tail = nhead
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right    
        return nhead.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nhead = ListNode(None)
        tail = nhead
        while True:
            index = -1
            for i, l in enumerate(lists):
                if l is None:
                    continue
                if index == -1 or lists[index].val > l.val:
                    index = i
            if index == -1:
                break
            tmp = lists[index]
            lists[index] = tmp.next
            if lists[index] is None:
                lists.pop(index)
            tail.next = tmp
            tail = tmp
        return nhead.next

            
