# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.cache = {}

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.treeHeight(root.left)
        right = self.treeHeight(root.right)
        ret = left + right
        ret = max(ret, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return ret

    def treeHeight(self, root):
        if root is None:
            return 0
        if root in self.cache:
            return self.cache[root]
        left = self.treeHeight(root.left)
        right = self.treeHeight(root.right)
        ret = 1 + max(left, right)
        self.cache[root] = ret
        return ret