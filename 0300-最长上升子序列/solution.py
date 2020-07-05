class Solution:
    # 动态规划
    def lengthOfLIS(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        length = 1
        for i in range(1, len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            length = max(length, dp[i])
        return length




    # 超出时间限制
    def lengthOfLIS0(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        length = 1
        for i in range(1, len(nums)):
            length = max(length, self.helper(nums[i-1], i, nums))
        return length
    
    def helper(self, basenum, index, nums):
        length = 1
        for i in range(index, len(nums)):
            if nums[i] > basenum:
                length = max(length, 1 + self.helper(nums[i], i+1, nums))
        return length

if __name__ == "__main__":
    test = [10, 9, 2, 5, 3, 4]
    res = Solution().lengthOfLIS(test)
    print(res)
