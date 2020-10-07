class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        if not nums or k <= 0:
            return ret
        window = []
        for i in range(k):
            if len(window) == 0:
                window.append(i)
                continue
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
        ret.append(nums[window[0]])
        for i in range(1, len(nums)-k+1):
            j = i + k - 1
            if window[0] < i or window[0] > j:
                window.pop(0)
            while window and nums[window[-1]] < nums[j]:
                window.pop()
            window.append[j]
            ret.append(nums[window[0]])
        return ret
    
    """
        超时
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        for i in range(len(nums)-k+1):
            tmp = nums[i:i+k]
            ret.append(max(tmp))
        return ret
