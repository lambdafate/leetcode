# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [link for link in lists if link]
        head = ListNode()
        tail = head
        while lists:
            index = 0
            for i, linklist in enumerate(lists):
                if linklist.val < lists[index].val:
                    index = i
            tmp = lists[index]
            lists[index] = tmp.next
            if lists[index] is None:
                lists.pop(index)
            tail.next = tmp
            tail = tail.next
        return head.next

