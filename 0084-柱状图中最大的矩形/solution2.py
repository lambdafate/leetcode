from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        low = min(heights)
        stack_forward = []
        stack_back = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            j = i + 1
            while j < len(stack_back) and heights[i] < heights[j]:
                j = stack_back[j]
            if j < len(stack_back) and heights[i] == heights[j]:
                j = stack_back[j]
            stack_back[i] = j
        for i in range(len(heights)):
            forward = -1
            while stack_forward and heights[i] <= heights[stack_forward[-1]]:
                stack_forward.pop()
            if stack_forward:
                forward = stack_forward[-1]
            back = stack_back[i]
            area = max(area, heights[i] * (back - forward - 1))
            stack_forward.append(i)
        return area



    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        low = min(heights)
        stack_forward = []
        # stack_back = []
        for i in range(len(heights)):
            forward, back = -1, len(heights)
            while stack_forward and heights[i] <= heights[stack_forward[-1]]: stack_forward.pop()
            if stack_forward:
                forward = stack_forward[-1]
            if heights[i] != low:
                back = i
                while back < len(heights) and heights[back] >= heights[i]: back += 1
            # while stack_back and heights[i] <= heights[stack_back[-1]]: stack_back.pop()
            # if stack_back:
            #     back = stack_back[-1]
            area = max(area, heights[i] * (back - forward - 1))
            stack_forward.append(i)
        return area
    """

    """
    # TLE
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            left, right = i, i
            while left >= 0 and heights[left] >= heights[i]: left -= 1
            while right < len(heights) and heights[i] <= heights[right]: right += 1
            area = max(area, heights[i] * (right - left - 1))
        return area
    """


a = [4, 2, 0, 3, 2, 4, 3, 4]
ans = Solution().largestRectangleArea(a)
print(ans)