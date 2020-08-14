# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        new_left = self.mirrorTree(root.left)
        new_right = self.mirrorTree(root.right)
        root.left, root.right = new_right, new_left
        return root
            
