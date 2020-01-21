class Solution:
    def searchRange(self, nums, target):
        left = self.find_left_index(nums, target)
        right = -1 if left == -1 else self.find_right_index(nums, target)
        return [left, right]

    def find_left_index(self, nums, target):
        left, right = 0, len(nums)-1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                return mid
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def find_right_index(self, nums, target):
        left, right = 0, len(nums)-1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                return mid
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1     
        return -1
