# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        queue = []
        result = []
        if root is None:
            return result
        queue.append(root)
        while queue:
            tmp = queue.pop(0)
            result.append(tmp.val)
            if tmp.left is not None:
                queue.append(tmp.left)
            if tmp.right is not None:
                queue.append(tmp.right)
        return result