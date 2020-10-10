# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        ret = self.check(root.left, root.right)
        return ret

    def check(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if (root1 and not root2) or (not root1 and root2):
            return False
        return root1.val == root2.val and self.check(root1.left, root2.right) and self.check(root1.right, root2.left)

        