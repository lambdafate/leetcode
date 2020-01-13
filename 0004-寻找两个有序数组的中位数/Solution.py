class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # extend 比 nums1+nums2 快很多
        nums1.extend(nums2)
        helper = nums1
        helper.sort()
        if len(helper)%2 == 0:
            # //为取整
            return (helper[len(helper)//2] + helper[len(helper)//2-1]) / 2
        return helper[len(helper)//2]





if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3], [2]))    