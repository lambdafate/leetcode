class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.backtrace(nums, [], ret)
        return ret
        
    def backtrace(self, nums, path, ret):
        if len(nums) == 0:
            ret.append(path)
            return
        norepeat = set()
        for i, num in enumerate(nums):
            if num in norepeat:
                continue
            norepeat.add(num)
            self.backtrace(nums[:i]+nums[i+1:], path+[num], ret)