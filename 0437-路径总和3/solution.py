# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sumNum: int) -> int:
        if root is None:
            return 0
        ret = self.paths(root, sumNum)
        ret += self.pathSum(root.left, sumNum)
        ret += self.pathSum(root.right, sumNum)
        return ret

    def paths(self, root, sumNum):
        if root is None:
            return 0
        ret = 0
        if root.val == sumNum:
            ret += 1
        sumNum = sumNum - root.val
        ret += self.paths(root.left, sumNum) + self.paths(root.right, sumNum)
        return ret
