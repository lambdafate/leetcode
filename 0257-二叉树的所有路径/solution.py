# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ret = []
        self.dfs(root, [], ret)
        ret = [ "->".join(path) for path in ret]
        return ret

    def dfs(self, root, path, ret):
        if root.left is None and root.right is None:
            path.append(str(root.val))
            ret.append(path)
            return None
        if root.left:
            self.dfs(root.left, path+[str(root.val)], ret)
        if root.right:
            self.dfs(root.right, path+[str(root.val)], ret)