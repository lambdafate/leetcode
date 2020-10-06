# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        nhead = TreeNode(None, root, None)
        # find target node
        work, prev = root, nhead
        while work:
            if work.val == key:
                break
            elif work.val < key:
                prev = work
                work = work.right
            else:
                prev = work
                work = work.left
        if work is None:
            return nhead.left
        linkNode = work.left
        if work.right:
            p = work.right
            while p.left:
                p = p.left
            p.left = linkNode
            linkNode = work.right
        if prev.left == work:
            prev.left = linkNode
        else:
            prev.right = linkNode
        return nhead.left