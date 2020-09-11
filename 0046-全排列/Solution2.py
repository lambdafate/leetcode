class Solution:
    def __init__(self):
        self.cache = {}

    """
        回溯
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.backtrace(nums, [], ret)
        return ret
    def backtrace(self, nums, path, ret):
        if len(nums) == 0:
            ret.append(path)
            return
        for i, num in enumerate(nums):
            self.backtrace(nums[:i]+nums[i+1:], path+[num], ret)




    """
        递归 + 缓存
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = self.recursion(nums, 0)
        return ret

    def recursion(self, nums, index):
        if index >= len(nums):
            return [[]]
        if index in self.cache:
            return [path[:] for path in self.cache[index]]
        next_ret = self.recursion(nums, index+1)
        ret = []
        for path in next_ret:
            for i in range(len(path)+1):
                tmp = path[:]
                tmp.insert(i, nums[index])
                ret.append(tmp)
        self.cache[index] = [path[:] for path in ret]
        return ret
