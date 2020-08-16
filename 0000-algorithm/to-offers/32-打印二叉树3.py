# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        result = []
        if root is None:
            return result
        i, reverse_line = 0, False
        while i < len(queue):
            line = [v.val for v in queue[i:]]
            if reverse_line:
                line = line[::-1]
            result.append(line)
            tmp = len(queue)
            for node in queue[i:]:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            i, reverse_line = tmp, not reverse_line
        return result


