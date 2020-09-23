# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        # delete root
        left = root.left
        root = root.right
        if not root:
            return left
        p = root
        while p.left:
            p = p.left
        p.left = left
        return root
        