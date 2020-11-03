# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ret = 0

    def sumNumbers(self, root: TreeNode) -> int:
        self.caculate(root, 0)
        return self.ret

    def caculate(self, root, prevSum):
        if root is None:
            return None
        tmp = prevSum * 10 + root.val
        if root.left is None and root.right is None:
            self.ret += tmp
        self.caculate(root.left, tmp)
        self.caculate(root.right, tmp)
        