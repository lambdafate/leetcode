"""
# 暴力 TLE
def solve(heights):
    ans = [0] * len(heights)
    for i in range(len(heights)):
        count = 1
        prev = float("-inf")
        for j in range(i - 1, -1, -1):
            if prev < heights[j]:
                count += 1
                prev = heights[j]
        prev = float("-inf")
        for j in range(i + 1, len(heights)):
            if prev < heights[j]:
                count += 1
                prev = heights[j]
        ans[i] = count
    return ans
"""

"""
# pass 40%
def solve(heights):
    if not heights: return []
    if len(heights) == 1: return [1]
    # init
    dp1 = [1] * len(heights)
    for i in range(1, len(dp1)):
        j = i - 1
        while j >= 0 and heights[i] >= heights[j]: j -= 1
        if j >= 0:
            dp1[i] += dp1[j]
    dp2 = [1] * len(heights)
    for i in range(len(dp2) - 2, -1, -1):
        j = i + 1
        while j < len(dp2) and heights[i] >= heights[j]: j += 1
        if j < len(dp2):
            dp2[i] += dp2[j]
    # solve
    ans = [1] * len(heights)
    ans[0] += dp2[1]
    ans[-1] += dp1[-2]
    for i in range(1, len(ans) - 1):
        ans[i] += dp1[i-1] + dp2[i+1]
    return ans
"""   

# 单调栈 100%
def solve(heights):
    if not heights:
        return []
    if len(heights) == 1:
        return [1]
    # init
    dp1 = [1] * len(heights)
    stack = [len(heights) - 1]
    for i in range(len(heights) - 2, -1, -1):
        while stack and heights[stack[-1]] <= heights[i]: stack.pop()
        if stack:
            dp1[i] += dp1[stack[-1]]
        stack.append(i)
    dp2 = [1] * len(heights)
    stack = [0]
    for i in range(1, len(heights)):
        while stack and heights[stack[-1]] <= heights[i]: stack.pop()
        if stack:
            dp2[i] += dp2[stack[-1]]
        stack.append(i)
    ans = [1] * len(heights)
    ans[0] += dp1[1]
    ans[-1] += dp2[-2]
    for i in range(1, len(ans) - 1):
        ans[i] += dp1[i+1] + dp2[i-1]
    return ans


if __name__ == "__main__":
    input()
    heights = [int(n) for n in input().split()]
    ans = solve(heights)
    for h in ans:
        print(h, end=" ")
