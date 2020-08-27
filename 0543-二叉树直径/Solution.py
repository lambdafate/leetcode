# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        Solution.res = 0
        self.treeDepth(root)
        return Solution.res

    def treeDepth(self, root):
        if not root:
            return 0
        l = self.treeDepth(root.left)
        r = self.treeDepth(root.right)
        Solution.res = max(Solution.res, l + r)
        return 1 + max(l, r)
