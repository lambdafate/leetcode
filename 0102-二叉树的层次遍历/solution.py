# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        queue = [root]
        while queue:
            values = []
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                values.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            ret.append(values)
        return ret