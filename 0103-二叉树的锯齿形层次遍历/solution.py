# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        queue = [root]
        reverse = False
        while queue:
            level = []
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            if reverse:
                level = level[::-1]
            reverse = not reverse
            ret.append(level)
        return ret