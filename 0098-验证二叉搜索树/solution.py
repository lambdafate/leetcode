# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ret = []
        self.helper(root, ret)
        for i in range(1, len(ret)):
            if ret[i-1] >= ret[i]:
                return False
        return True

    def helper(self, root, ret):
        if not root:
            return
        self.helper(root.left, ret)
        ret.append(root.val)
        self.helper(root.right, ret)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.validValue(root.left, root.val, True) and self.isValidBST(root.left)
        right = left and self.validValue(root.right, root.val, False) and self.isValidBST(root.right)
        return left and right

    def validValue(self, root, value, bigger):
        if not root:
            return True
        if bigger and root.val >= value:
            return False
        if not bigger and root.val <= value:
            return False
        return self.validValue(root.left, value, bigger) and self.validValue(root.right, value, bigger)
        
        
