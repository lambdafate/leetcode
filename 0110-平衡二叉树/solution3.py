# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.cache = {}

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        l = self.treeHeight(root.left)
        r = self.treeHeight(root.right)
        if abs(l - r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def treeHeight(self, root):
        if root is None:
            return 0
        if root in self.cache:
            return self.cache[root]
        left = self.treeHeight(root.left)
        right = self.treeHeight(root.right)
        ret = 1 + max(left, right)
        self.cache[root] = ret
        return ret