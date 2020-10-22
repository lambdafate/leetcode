from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ret = []
        if root is None:
            return ret
        queue = deque()
        queue.append(root)
        while queue:
            ret.append(queue[-1].val)
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        return ret