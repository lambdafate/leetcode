# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        快慢指针定位后半链表, 后半链表反转, 最后依次插入前半部分
    """
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        nhead = slow.next
        slow.next = None
        nhead = self.reverseList(nhead)
        work = head
        while nhead:
            tmp = nhead
            nhead = nhead.next
            tmp.next = work.next
            work.next = tmp
            work = work.next.next
        return None
    
    def reverseList(self, head):
        """
            反转链表
        """
        nhead = None
        while head:
            tmp = head
            head = head.next
            tmp.next = nhead
            nhead = tmp
        return nhead