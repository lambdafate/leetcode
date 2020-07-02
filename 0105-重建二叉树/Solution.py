# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):

        def helper(pindex0, pindex1, iindex0, iindex1):
            if pindex1 < pindex0:
                return None
            r = TreeNode(preorder[pindex0])
            index = inorder.index(preorder[pindex0])
            r.left = helper(pindex0+1, index-iindex0+pindex0, iindex0, index-1)
            r.right = helper(pindex1+index+1-iindex1,
                             pindex1, index+1, iindex1)
            return r

        root = helper(0, len(preorder)-1, 0, len(inorder)-1)
        return root
