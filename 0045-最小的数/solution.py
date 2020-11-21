from functools import cmp_to_key

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def cmp_rule(x, y):
            a = x + y
            b = y + x
            if a < b: return -1
            elif a > b: return 1
            return 0
        nums.sort(key=cmp_to_key(cmp_rule))
        return "".join(nums)


    """
        dfs 超时
    """
    def __init__(self):
        self.ret = ""

    def minNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        nums = [str(num) for num in nums]
        nums.sort()
        self.dfs(nums, "")
        return self.ret

    def dfs(self, nums, prevSum):
        if not nums:
            if not self.ret or int(prevSum) < int(self.ret):
                self.ret = prevSum
            return
        c = nums[0][0]
        cache = set()
        for i, num in enumerate(nums):
            if num in cache:
                continue
            if num[0] != c:
                break
            cache.add(num)
            self.dfs(nums[:i] + nums[i+1:], prevSum + str(num))
