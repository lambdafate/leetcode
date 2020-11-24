# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if self.subPathFromRoot(head, node):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def subPathFromRoot(self, head, root):
        if not root or not head:
            return head == root
        if head.val != root.val:
            return False
        if not head.next:
            return True
        return self.subPathFromRoot(head.next, root.left) or self.subPathFromRoot(head.next, root.right)
