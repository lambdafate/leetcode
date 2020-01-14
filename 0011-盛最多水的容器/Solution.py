# 双指针
class Solution:
    def maxArea(self, height):
        low, high = 0, len(height)-1
        res = 0
        while(low < high):
            temp = 0
            if height[low] <= height[high]:
                temp = height[low]
                low = low + 1
            else:
                temp = height[high]
                high = high - 1
            
            temp = (high-low + 1) * temp
            if temp > res:
                res = temp
        return res