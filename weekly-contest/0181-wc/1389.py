class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret = []
        for num, i in zip(nums, index):
            ret.insert(i, num)
        return ret
