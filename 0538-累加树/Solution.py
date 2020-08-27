# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.convert(root, 0)
        return root

    def convert(self, root, basenum):
        rightSum = self.sumNum(root.right)
        self.convert(root.left, basenum + root.val + rightSum)
        self.convert(root.right, basenum)
        root.val += basenum + rightSum

    def sumNum(self, root):
        if not root:
            return 0
        return root.val + self.sumNum(root.left) + self.sumNum(root.right)