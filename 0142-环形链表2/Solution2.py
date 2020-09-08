# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
        检测链表是否有环, 并返回入环节点
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # slow and fast meeting
            if slow == fast:
                fast = head
                while fast != slow:
                    slow, fast = slow.next, fast.next
                return fast
        return None