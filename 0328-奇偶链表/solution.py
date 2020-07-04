# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head, even_head = ListNode(0), ListNode(0)
        odd_tail, even_tail = odd_head, even_head
        flag = True
        while head:
            if flag:
                odd_tail.next = head
                odd_tail = odd_tail.next
            else:
                even_tail.next = head
                even_tail = even_tail.next
            flag = not flag
            head = head.next
        even_tail.next = None
        odd_tail.next = even_head.next
        return odd_head.next