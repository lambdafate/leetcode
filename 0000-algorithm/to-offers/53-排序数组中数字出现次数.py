class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if l > r:
            return 0
        res = 0
        for num in nums[mid::-1]:
            if num != target:
                break
            res += 1
        for num in nums[mid:]:
            if num != target:
                break
            res += 1
        return res-1