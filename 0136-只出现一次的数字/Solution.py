class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret = ret ^ num
        return ret


    def singleNumber(self, nums: List[int]) -> int:
        helper = {}
        for num in nums:
            if num not in helper:
                helper[num] = 0
            helper[num] += 1
        for k, v in helper.items():
            if v == 1:
                return k
        return None
