# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        curr = root
        stack = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            while stack and curr is None:
                curr = stack.pop()
                ret.append(curr.val)
                curr = curr.right
        return ret