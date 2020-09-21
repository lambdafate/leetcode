# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        if n <= 0:
            return []
        nums = list(range(1, n+1))
        ret = self.recursion(nums)
        return ret

    def recursion(self, nums):
        if not nums:
            return [None]
        ret = []
        for i, num in enumerate(nums):
            left = self.recursion(nums[:i])
            right = self.recursion(nums[i+1:])
            for left_node in left:
                for right_node in right:
                    tmp = TreeNode(num, left=left_node, right=right_node)
                    ret.append(tmp)
        return ret

ret = Solution().generateTrees(1)
for i in ret:
    print(i)

        
