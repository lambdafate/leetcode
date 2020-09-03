# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """ 
        快慢指针
    """
    def detectCycle(self, head):
        if head is None:
            return None
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            # 相遇
            if slow is fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None



    """
    # 使用哈希表
    def detectCycle(self, head: ListNode) -> ListNode:
        cache = set()
        p = head
        while p:
            if p in cache:
                return p
            cache.add(p)
            p = p.next
        return None
    """