# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root
    
    
    """
        1
    """
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if self.check(root):
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root

    def check(self, root):
        if root is None:
            return True
        return root.val == 0 and self.check(root.left) and self.check(root.right)
