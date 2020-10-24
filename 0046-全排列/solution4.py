class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums, [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        if not nums:
            ret.append(path)
            return None
        for i, num in enumerate(nums):
            self.dfs(nums[:i]+nums[i+1:], path+[num], ret)
        