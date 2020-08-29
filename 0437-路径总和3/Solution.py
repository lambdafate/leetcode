# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.allPaths(root, sum)
        
    def allPaths(self, root, sumNum):
        if root is None:
            return 0
        tmp = sumNum - root
        ret = 1 if tmp == 0 else 0
        ret += self.allPaths(root.left, tmp) + self.allPaths(root.right, tmp)
        return ret + self.allPaths(root.left, sumNum) + self.allPaths(root.right, sumNum)
