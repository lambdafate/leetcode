"""
    两个一组反转链表
"""
from random import randint

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solution(head):
    nhead = None
    while head and head.next:
        temp_head, temp_tail = head, head.next
        head = temp_tail.next
        temp_tail.next = nhead
        nhead = temp_head
    if head is None:
        return nhead
    head.next = nhead
    return head


if __name__ == "__main__":
    head = Node(0)
    tail = head
    for i in range(1, randint(5, 10)):
        tail.next = Node(i)
        tail = tail.next
    tmp = head
    while tmp is not None:
        print(f"{tmp.val} => ", end="")
        tmp = tmp.next
    print("")

    nhead = solution(head)
    while nhead is not None:
        print(f"{nhead.val} => ", end="")
        nhead = nhead.next
    print("None")
