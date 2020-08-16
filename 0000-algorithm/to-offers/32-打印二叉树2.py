# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = [root]
        if root is None:
            return result
        i = 0
        while i < len(queue):
            result.append([v.val for v in queue[i:]])
            tmp = len(queue)
            for node in queue[i:]:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            i = tmp
        return result