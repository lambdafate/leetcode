"""
    二叉树, 非递归中序遍历
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        work = root
        nodes = []
        res = []
        while work is not None or len(nodes) != 0:
            while work is not None:
                nodes.append(work)
                work = work.left
                continue

            work = nodes.pop()
            res.append(work.val)
            
            while work.right is None and len(nodes) != 0:
                work = nodes.pop()
                res.append(work.val)

            if work.right is not None:
                work = work.right
            else:
                break
        return res

