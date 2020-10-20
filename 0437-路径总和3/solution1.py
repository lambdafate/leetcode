# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        ret = self.rootPaths(root, sum)
        ret += self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return ret

    def rootPaths(self, root, sumNum):
        if root is None:
            return 0
        ret = 1 if root.val == sumNum else 0
        ret += self.rootPaths(root.left, sumNum-root.val) + self.rootPaths(root.right, sumNum-root.val)
        return ret