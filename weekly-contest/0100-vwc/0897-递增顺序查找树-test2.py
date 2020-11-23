# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.increasingBST(root.left)
        right = self.increasingBST(root.right)
        # update root node
        root.left = None
        root.right = right
        if left is None:
            return root
        work = left
        while work.right:
            work = work.right
        work.right = root
        return left
