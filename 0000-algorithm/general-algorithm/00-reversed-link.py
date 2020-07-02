class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solution(head):
    nhead = None
    while head is not None:
        temp, head = head, head.next
        temp.next = nhead
        nhead = temp
    return nhead


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

    nhead = solution2(head)
    while nhead is not None:
        print(f"{nhead.val} => ", end="")
        nhead = nhead.next
    print("None")
