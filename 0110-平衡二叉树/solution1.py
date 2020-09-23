# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.cache = {}

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return (abs(left_height-right_height) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if not node:
            return 0
        if node in self.cache:
            return self.cache[node]
        ret = 1 + max(self.height(node.left), self.height(node.right))
        self.cache[node] = ret
        return ret