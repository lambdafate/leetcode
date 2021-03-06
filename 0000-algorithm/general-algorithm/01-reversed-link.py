class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 1 -> 2 -> 3
# 3 -> 2 -> 1
# 迭代法
def solution(head):
    nhead = None
    while head is not None:
        tmp = head
        head = head.next
        tmp.next = nhead
        nhead = tmp
    return nhead

# 迭代法
def solution1(head):
    prev = Node(0)
    prev.next = head
    while head and head.next:
        tmp = head.next
        head.next = tmp.next
        tmp.next = prev.next
        prev.next = tmp
    return prev.next



# 递归法
def solution2(head):
    nhead = Node(-1)
    work = nhead

    def helper(node):
        nonlocal work
        if node is None:
            return None
        elif node.next is None:
            work.next = node
            work = node
            return None
        helper(node.next)
        node.next = None
        work.next = node
        work = node
    helper(head)
    return nhead.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    nhead = solution1(head)
    while nhead is not None:
        print(f"{nhead.val} => ", end="")
        nhead = nhead.next
    print("None")
