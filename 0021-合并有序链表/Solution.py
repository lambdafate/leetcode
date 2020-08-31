# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        curr = head
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return head.next


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 if l1 else l2
        helper = []
        head = l1
        while l1.next:
            helper.append(l1.val)
            l1 = l1.next
        l1.next = l2
        while l1:
            helper.append(l1.val)
            l1 = l1.next
        helper = sorted(helper)
        p = head
        for n in helper:
            p.val = n
            p = p.next
        return head

if __name__ == "__main__":
    t1 = ListNode(1, ListNode(2, ListNode(4)))
    t2 = ListNode(1, ListNode(3, ListNode(4)))
    Solution().mergeTwoLists(t1, t2)
