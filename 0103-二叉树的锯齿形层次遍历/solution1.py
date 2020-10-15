from collections import deque

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
        queue = deque()
        queue.append(root)
        reverse = False
        while queue:
            level = deque()
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if reverse:
                    level.appendleft(tmp.val)
                else:
                    level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            ret.append(list(level))
            reverse = not reverse
        return ret
