class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    num = nums[l]
                    while l < r and nums[l] == num:
                        l += 1
                    num = nums[r]
                    while l < r and nums[r] == num:
                        r -= 1
                elif tmp < 0:
                    l += 1
                else:
                    r -= 1
        return ret
