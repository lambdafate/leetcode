# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.cache = {}

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if root is None:
            return 0
        if root in self.cache:
            return self.cache[root]
        left = self.height(root.left)
        right = self.height(root.right)
        ret = 1 + max(left, right)
        self.cache[root] = ret
        return ret