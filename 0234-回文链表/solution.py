# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow, fast = head, None
        if head:
            fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        work = slow.next
        nhead = None
        while work:
            tmp = work
            work = work.next
            tmp.next = nhead
            nhead = tmp
        while nhead:
            if nhead.val != head.val:
                return False
            nhead = nhead.next
            head = head.next
        return True
    
    
    def isPalindrome(self, head: ListNode) -> bool:
        chars = []
        p = head
        while p:
            chars.append(p.val)
            p = p.next
        i, j = 0, len(chars)-1
        while i <= j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1
        return True
