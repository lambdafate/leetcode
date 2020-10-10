# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right or None


    def __init__(self):
        self.cache = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        self.initNode(root)
        ret = self.recursion(root, p, q)
        return ret
    
    def recursion(self, root, p, q):
        if root is None:
            return None
        if root is p or root is q:
            return root
        left = -1 if root.left and p in self.cache[root.left] else 1
        right = -1 if root.left and q in self.cache[root.left] else 1
        if left != right:
            return root
        if left == -1:
            return self.recursion(root.left, p, q)
        return self.recursion(root.right, p, q)


    def initNode(self, root):
        if root is None:
            return set()
        if root in self.cache:
            return self.cache[root]
        left = self.initNode(root.left)
        right = self.initNode(root.right)
        ret = set()
        ret.add(root)
        self.cache[root] = ret | left | right
        return self.cache[root]

if __name__ == "__main__":
    pass
