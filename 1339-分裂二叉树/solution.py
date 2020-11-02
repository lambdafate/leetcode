# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.cache = {}

    def maxProduct(self, root: TreeNode) -> int:
        if root is None:
            return 0
        allSum = self.treeSum(root)
        ret = 0
        for node, nodeSum in self.cache.items():
            if node is not root:
                ret = max(ret, nodeSum * (allSum - nodeSum))
        return ret % (10**9 + 7)

    def treeSum(self, root):
        if root is None:
            return 0
        if root in self.cache:
            return self.cache[root]
        ret = root.val
        ret += self.treeSum(root.left) + self.treeSum(root.right)
        self.cache[root] = ret
        return ret
