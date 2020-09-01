class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = self.trace(nums, 0)
        return ret

    def trace(self, nums, index):
        if index >= len(nums):
            return [[]]
        ret = self.trace(nums, index+1)
        old_length = len(ret)
        for i in range(old_length):
            length = len(ret[i]) + 1
            for j in range(length):
                tmp = ret[i][:]
                tmp.insert(j, nums[index])
                ret.append(tmp)
        ret = ret[old_length:]
        return ret