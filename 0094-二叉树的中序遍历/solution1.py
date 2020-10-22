# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        if root is None:
            return ret
        stack = []
        work = root
        while work or stack:
            while work:
                stack.append(work)
                work = work.left
            while stack and work is None:
                work = stack.pop()
                ret.append(work.val)
                work = work.right
        return ret
