class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper = {}
        res = [0, 0]
        for i, num in enumerate(nums):
            if num in helper:
                res[0], res[1] = helper[num], i
                break
            helper[target-num] = i
        return res
