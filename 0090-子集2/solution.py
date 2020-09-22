class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()   # this is must
        self.backtrace(nums, [], ret)
        return ret

    def backtrace(self, nums, path, ret):
        ret.append(path)
        if not nums:
            return
        used = set()
        for i, num in enumerate(nums):
            if num in used:
                continue
            used.add(num)
            self.backtrace(nums[i+1:], path+[num], ret)