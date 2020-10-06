class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] < 0:
                ret.append(abs(nums[j]))
            nums[j] = -nums[j]
        return ret

    def findDuplicates(self, nums: List[int]) -> List[int]:
        helper = {}
        for num in nums:
            if num not in helper:
                helper[num] = 0
            helper[num] += 1
        ret = []
        for k, v in helper.items():
            if v == 2:
                ret.append(k)
        return ret
