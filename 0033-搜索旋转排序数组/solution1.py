class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid] >= nums[j]:
                    i = mid + 1
                else:
                    if target <= nums[j]:
                        i = mid + 1
                    else:
                        j = mid - 1
            else:
                if nums[mid] <= nums[j]:
                    j = mid - 1
                else:
                    if target >= nums[i]:
                        j = mid - 1
                    else:
                        i = mid + 1
        return -1