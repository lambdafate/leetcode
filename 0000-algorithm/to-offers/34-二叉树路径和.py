# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        result = []
        if root is None:
            return result
        if root.left is None and root.right is None:
            if root.val == target:
                result.append([target])
            return result
        left = self.pathSum(root.left, target-root.val)
        right = self.pathSum(root.right, target-root.val)
        left.extend(right)
        paths = left
        for path in paths:
            path.insert(0, root.val)
        return paths

