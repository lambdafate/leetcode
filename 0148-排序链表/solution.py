# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # fast-slow pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(tmp)
        return self.mergeLinkList(left, right)

    def mergeLinkList(self, head1, head2):
        nhead = ListNode(None)
        work = nhead
        while head1 and head2:
            if head1.val < head2.val:
                tmp = head1
                head1 = head1.next
                work.next = tmp
            else:
                tmp = head2
                head2 = head2.next
                work.next = tmp
            work = work.next
        work.next = head1 if head1 else head2
        return nhead.next