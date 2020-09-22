class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.backtrace(nums, [], ret)
        return ret

    def backtrace(self, nums, path, ret):
        if not nums:
            ret.append(path)
            return
        for i, num in enumerate(nums):
            tmp = nums[:i] + nums[i+1:]
            self.backtrace(tmp, path+[num], ret)