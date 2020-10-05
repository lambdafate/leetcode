# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ret = []
        self.dfs(root, sum, [], ret)
        return ret

    def dfs(self, root, target, path, ret):
        if root.left is None and root.right is None:
            if target == root.val:
                ret.append(path+[root.val])
            return None
        if root.left:
            self.dfs(root.left, target-root.val, path+[root.val], ret)
        if root.right:
            self.dfs(root.right, target-root.val, path+[root.val], ret)
        return None