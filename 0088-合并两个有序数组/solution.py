class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        last = m
        while i < last and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
                continue
            index = last
            while index > i:
                nums1[index] = nums1[index-1]
                index -= 1
            last += 1
            nums1[i] = nums2[j]
            i += 1
            j += 1
        for i in range(j, n):
            nums1[last] = nums2[i]
            last += 1
        return None