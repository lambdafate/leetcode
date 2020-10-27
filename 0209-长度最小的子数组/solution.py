class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j = 0, 0
        ret = float("inf")
        trimSum = 0
        while j < len(nums):
            while trimSum < s and j < len(nums):
                trimSum += nums[j]
                j += 1
            while trimSum >= s:
                ret = min(ret, j-i)
                trimSum -= nums[i]
                i += 1
        """
        while j <= len(nums):
            if trimSum < s:
                if j >= len(nums):
                    break 
                trimSum += nums[j]
                j += 1
            else:
                ret = min(ret, j - i)
                trimSum -= nums[i]
                i += 1
        """
        return 0 if ret == float("inf") else ret        

    """
        暴力
    """
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ret = float("inf")
        for i in range(len(nums)):
            tmp = 0
            flag = True
            for j in range(i, len(nums)):
                tmp += nums[j]
                if tmp >= s:
                    ret = min(ret, j-i+1)
                    flag = False
                    break
            if flag:
                break
        return 0 if ret == float("inf") else ret
