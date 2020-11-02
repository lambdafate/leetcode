# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
        迭代
    """
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ret = 0
        stack = []
        work = root
        while work:
            head = work
            while work.left:
                stack.append(work)
                work = work.left
            if work is not head and work.right is None:
                ret += work.val
            work = work.right
            while stack and work is None:
                tmp = stack.pop()
                work = tmp.right
        return ret





    def __init__(self):
        self.ret = 0
    """
        递归先序遍历
    """
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.prevOrder(root, False)
        return self.ret
        
    def prevOrder(self, root, flag):
        if root is None:
            return None
        if flag and root.left is None and root.right is None:
            self.ret += root.val
        else:
            self.prevOrder(root.left, True)
            self.prevOrder(root.right, False)
