# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root]
        index = 0
        while index < len(queue):
            tmp = queue[index]
            if tmp:
                queue.append(tmp.left)
                queue.append(tmp.right)
            index += 1
        for i in range(len(queue)):
            if queue[i] is None:
                index = i
                break
        for i in range(index+1, len(queue)):
            if queue[i] is not None:
                return False
        return True

    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root]
        flag = False
        while queue:
            tmp = queue.pop(0)
            if tmp.left:
                if flag:
                    return False
                queue.append(tmp.left)
            else:
                flag = True
            if tmp.right:
                if flag:
                    return False
                queue.append(tmp.right)
            else:
                flag = True
        return True
