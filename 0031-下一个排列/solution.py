class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in range(len(nums)-1, -1, -1):
            index = -1
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                if index == -1 or nums[j] <= nums[index]:
                    index = j
            if index != -1:
                nums[i], nums[index] = nums[index], nums[i]
                k = i
                break
        self.reverseList(nums, k + 1, len(nums) - 1)
        return None

    def reverseList(self, nums, begin, end):
        i, j = begin, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return None


if __name__ == "__main__":
    nums = [1, 2, 3]
    ret = Solution().nextPermutation(nums)
    print(nums)
