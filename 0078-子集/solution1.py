class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ret = self.subsets(nums[1:])
        tmp = []
        for v in ret:
            t = v.copy()
            t.append(nums[0])
            tmp.append(t)
        ret.extend(tmp)
        return ret


    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.backtrace(nums, [], ret)
        return ret

    def backtrace(self, nums, path, ret):
        ret.append(path)
        if not nums:
            return
        for i, num in enumerate(nums):
            self.backtrace(nums[i+1:], path+[num], ret)
