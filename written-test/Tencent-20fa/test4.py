days = int(input())
# tmp = input().split()
# company = tmp[:days]
# ktv = tmp[days:]
company = input().split()
ktv = input().split()

OPEN = '1'
CLOSE = '0'

SLEEP = 0
WORK = 1
FUCK = 2

def solve():
    if days <= 0: return 0
    dp = [[float("inf")] * 3 for _ in range(days)]
    dp[0][SLEEP] = 1
    if company[0] == OPEN:
        dp[0][WORK] = 0
    if ktv[0] == OPEN:
        dp[0][FUCK] = 0
    for i in range(1, len(dp)):
        # sleep
        dp[i][SLEEP] = 1 + min(dp[i-1][SLEEP], dp[i-1][WORK], dp[i-1][FUCK])
        # work
        if company[i] == OPEN:
            dp[i][WORK] = min(dp[i-1][SLEEP], dp[i-1][FUCK])
        # fuck
        if ktv[i] == OPEN:
            dp[i][FUCK] = min(dp[i-1][SLEEP], dp[i-1][WORK])
    return min(dp[-1])

print(solve())

"""
cache = {}
try:
    def dfs(day, action):
        if day >= days: return 0
        if (action == WORK and company[day] == CLOSE) or (action == FUCK and ktv[day] == CLOSE):
            return float("inf")
        global cache
        k = (day, action)
        if k in cache:
            return cache[k]
        times = None
        if action == SLEEP:
            times = 1 + min(dfs(day + 1, WORK), dfs(day + 1, SLEEP), dfs(day + 1, FUCK))
        else:
            times = min(dfs(day + 1, SLEEP), dfs(day + 1, -action))
        cache[k] = times
        return times

    ans = min(dfs(0, WORK), dfs(0, SLEEP), dfs(0, FUCK))
    print(ans)
except Exception as e:
    print("\n<br> ERROR<br>\n")
    print(e)
    print(f"\ncompany:\n{company}")
    print(f"\nktv:\n{ktv}\n")
"""
