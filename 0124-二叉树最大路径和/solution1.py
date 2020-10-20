# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.cache = {}

    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ret = root.val + max(0, self.rootPath(root.left)) + max(0, self.rootPath(root.right))
        if root.left:
            ret = max(ret, self.maxPathSum(root.left))
        if root.right:
            ret = max(ret, self.maxPathSum(root.right))
        return ret
    def rootPath(self, root):
        if root is None:
            return 0
        if root in self.cache:
            return self.cache[root]
        ret = root.val
        left = self.rootPath(root.left)
        right = self.rootPath(root.right)
        ret = ret + max(0, left, right)
        self.cache[root] = ret
        return ret