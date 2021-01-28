class Solution:
    """
        单调栈
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        # 向前查找较小高度
        stack = [-1]
        # 最后清除单调栈中所有元素
        heights.append(float("-inf"))
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()
                area = max(area, heights[j] * (i - stack[-1] - 1))
            stack.append(i)
        return area
