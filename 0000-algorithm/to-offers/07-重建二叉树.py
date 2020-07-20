# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = self.rebuild(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        return root
    
    def rebuild(self, preorder, pb, pe, inorder, ib, ie):
        if pb > pe:
            return None
        root = TreeNode(preorder[pb])
        i = ib
        while i <= ie:
            if inorder[i] == preorder[pb]:
                break
            i += 1
        root.left = self.rebuild(preorder, pb+1, i-ib+pb, inorder, ib, i-1)
        root.right = self.rebuild(preorder, pe-ie+i+1, pe, inorder, i+1, ie)
        return root

