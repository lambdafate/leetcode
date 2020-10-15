# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        if self.equalTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def equalTree(self, s, t):
        if s is None or t is None:
            return s is t
        # print(f"{s.val} -- {t.val}")
        if s.val != t.val:
            return False
        return self.equalTree(s.left, t.left) and self.equalTree(s.right, t.right)

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(1), TreeNode(2))
    Solution().isSubtree(root, root)