# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [root]
        count = 0
        while queue:
            count += 1
            tmp = queue.pop(0)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return count
