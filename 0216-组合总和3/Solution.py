class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        ret = []
        self.backtrace(nums, 0, [], ret, n, k)
        return ret
    def backtrace(self, nums, index, path, ret, target, length):
        if target < 0:
            return
        if target == 0:
            if len(path) == length:
                ret.append(path)
            return
        if len(path) >= length:
            return
        for i in range(index, len(nums)):
            if nums[index] > target:
                break
            self.backtrace(nums, i+1, path+[nums[i]], ret, target-nums[i], length)
