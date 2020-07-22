class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if abs(target-res) > abs(target-tmp):
                    res = tmp
                if tmp > target:
                    r -= 1
                elif tmp < target:
                    l += 1
                else:
                    return tmp
        return res
