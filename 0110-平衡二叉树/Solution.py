# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):

        def check(node):
            if node is None:
                return 0
            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right)+1

        res = check(root)
        return res != -1
