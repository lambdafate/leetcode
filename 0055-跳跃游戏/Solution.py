class Solution:
    def __init__(self):
        self.cache = {}

    # 贪心
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if nums[0] <= 0:
            return len(nums) == 1
        fastest = -1
        for pos, jump_length in enumerate(nums):
            if jump_length == 0:
                if fastest > pos:
                    continue
                return pos == (len(nums)-1)
            fastest = max(fastest, pos+jump_length)
            if fastest >= (len(nums)-1):
                return True
        return False


    """
    # 优化的动态规划(这个跑的时间更长, 捂脸.jpg)
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        dp = [False] * len(nums)
        dp[0] = True
        queue = [0]
        for i in range(1, len(nums)):
            for j in range(len(queue)-1, -1, -1):
                if (j+nums[j]) >= i:
                    dp[i] = True
                    queue.append(i)
                    break
        return dp[-1]

    """

    """
    # 动态规划
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] and (j+nums[j]) >= i:
                    dp[i] = True
                    break
        return dp[-1]
    """
    
    
    """
    def canJump(self, nums: List[int]) -> bool:
        can_jump = self.caJumpFromPos(nums, 0)
        return can_jump

    def caJumpFromPos(self, nums, pos):
        if pos >= len(nums):
            return True
        if nums[pos] <= 0:
            return pos == (len(nums)-1)
        if pos in self.cache:
            return self.cache[pos]
        ret = False
        for jump_pos in range(pos+nums[pos], pos, -1):
            if self.caJumpFromPos(nums, jump_pos):
                ret = True
                break
        self.cache[pos] = ret
        return ret
    """
