class Solution:
    # 动态规划
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]
 
    # 迭代, 实时维护可以到达的最远位置
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for i, num in enumerate(nums):
            if i > maxIndex:
                break
            tmp = i + num
            maxIndex = max(maxIndex, tmp)
            if maxIndex >= len(nums)-1:
                return True
        return False
    """
    # 递归 超时
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        cache = set()
        ret = self.dfs(nums, 0, cache)
        return ret

    def dfs(self, nums, i, cache):
        if i == len(nums)-1:
            return True
        if nums[i] == 0 or i in cache:
            return False
        step = nums[i]
        if i + step >= len(nums)-1:
            return True
        for j in range(i+step, i, -1):
            if self.dfs(nums, j, cache):
                return True
        cache.add(i)
        return False
    """
