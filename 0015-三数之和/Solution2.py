class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        used = set()
        for i, num in enumerate(nums):
            if num in used:
                continue
            if num > 0:
                break
            used.add(num)
            result = self.twoSum(nums, i+1, -num)
            for path in result:
                tmp = path[:]
                tmp.append(num)
                ret.append(tmp)
        return ret

    def twoSum(self, nums, index, target):
        helper = {}
        ret = []
        norepeat = set()
        for i in range(index, len(nums)):
            if nums[i] in helper and nums[i] not in norepeat:
                ret.append([nums[i], nums[helper[nums[i]]]])
                norepeat.add(nums[i])
                norepeat.add(nums[helper[nums[i]]])
                continue
            helper[target-nums[i]] = i
        return ret
