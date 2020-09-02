# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        1. p, q 都在 root.left
        2. p, q 都在 root.right
        3. p, q 一个在 root.left，一个在 root.right
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if p is root or q is root:
            curr = root
            another = q if p is root else p
            if self.alive(curr.left, another) or self.alive(curr.right, another):
                return curr
            return None
        ret0 = self.lowestCommonAncestor(
            root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
        return ret0 or (root if self.alive(root, p) and self.alive(root, q) else None)

    def alive(self, root, target):
        if root is None:
            return False
        if root is target:
            return True
        return self.alive(root.left, target) or self.alive(root.right, target)
