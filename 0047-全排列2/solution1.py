class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        self.backtrace(nums, [], ret)
        return ret

    def backtrace(self, nums, path, ret):
        if not nums:
            ret.append(path)
            return None
        used = set()
        for i, num in enumerate(nums):
            if num in used:
                continue
            used.add(num)
            self.backtrace(nums[:i]+nums[i+1:], path+[num], ret)