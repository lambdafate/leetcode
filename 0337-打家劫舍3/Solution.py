# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.cache = {}
    """
        不用cache直接超时, 用了cache 直接Beat 88% 
    """
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root in self.cache:
            return self.cache[root]
        rob1 = root.val
        if root.left:
            rob1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            rob1 += self.rob(root.right.left) + self.rob(root.right.right)
        rob2 = self.rob(root.left) + self.rob(root.right)
        ret = max(rob1, rob2)
        self.cache[root] = ret
        return ret