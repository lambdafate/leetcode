# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None or t2 is None:
            return t1 if t1 else t2
        t1.val += t2.val
        left = self.mergeTrees(t1.left, t2.left)
        right = self.mergeTrees(t1.right, t2.right)
        t1.left, t1.right = left, right
        return t1 