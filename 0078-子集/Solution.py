class Solution:
    # 循环
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for num in nums:
            for i in range(len(ret)):
                tmp = ret[i][::]
                tmp.append(num)
                ret.append(tmp)
            ret.append([num])
        ret.append([])
        return ret

        
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = self.helper(nums, 0)
        ret.append([])
        return ret
    # 倒序
    def helper(self, nums, index):
        if index >= len(nums):
            return []
        ret = self.helper(nums, index+1)
        for i in range(len(ret)):
            tmp = ret[i][::]
            tmp.append(nums[index])
            ret.append(tmp)
        ret.append([nums[index]])
        return ret
    """

    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0, [])
    
    # 正序
    def helper(self, nums, index, ret):
        if index >= len(nums):
            ret.append([])
            return ret
        for i in range(len(ret)):
            tmp = ret[i][::]
            tmp.append(nums[index])
            ret.append(tmp)
        ret.append([nums[index]])
        return self.helper(nums, index+1, ret)
    """
