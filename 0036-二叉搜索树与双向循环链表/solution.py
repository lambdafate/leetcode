# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        left_head = self.treeToDoublyList(root.left)
        right_head = self.treeToDoublyList(root.right)
        head = left_head or root
        tail = right_head.left if right_head else root
        if left_head:
            left_head.left.right = root
            root.left = left_head.left
        if right_head:
            right_head.left = root
            root.right = right_head
        head.left = tail
        tail.right = head
        return head


