class Solution:
    def findUnsortedSubarray(self, nums):
        if len(nums) < 2:
            return 0
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] > nums[j]:
                break
            flag = True
            if nums[i] <= nums[i+1]:
                i += 1
                flag = False
            if nums[j-1] <= nums[j]:
                j -= 1
                flag = False
            if flag:
                break

        print("fuck")
        if i >= j:
            return 0
        maxNum, minNum = max(nums[i:j+1]), min(nums[i:j+1])
        i, j = i-1, j+1
        while i >= 0 and nums[i] > minNum:
            i -= 1
        while j < len(nums) and nums[j] < maxNum:
            j += 1
        return j - i - 1 

if __name__ == "__main__":
    n = [2, 6, 4, 8, 10, 9, 15]
    Solution().findUnsortedSubarray(n)
