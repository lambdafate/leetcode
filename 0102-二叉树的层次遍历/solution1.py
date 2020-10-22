from collections import deque

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
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                tmp = queue.popleft()
                level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            ret.append(level)
        return ret