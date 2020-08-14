# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A is None or B is None:
            return False
        if self.helper(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def helper(self, source, target):
        if source is None or target is None or target.val != source.val:
            return False
        res = True
        if target.left is not None:
            res = self.helper(source.left, target.left)
        if res and target.right is not None:
            res = self.helper(source.right, target.right)
        return res