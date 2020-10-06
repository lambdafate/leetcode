# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.cache = {}

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return float("-inf")
        left = self.maxTreeNum(root.left)
        right = self.maxTreeNum(root.right)
        tmp = root.val + max(0, left) + max(0, right)
        ret = max(tmp, self.maxPathSum(root.left), self.maxPathSum(root.right))
        return ret

    def maxTreeNum(self, root):
        if not root:
            return 0
        if root in self.cache:
            return self.cache[root]
        left = self.maxTreeNum(root.left)
        right = self.maxTreeNum(root.right)
        ret = root.val + max(0, left, right)
        self.cache[root] = ret
        return ret
