source = input()
encode = {"0", "1", "10", "11", "100", "101", "110", "111"}

def solve(source):
    if len(source) <= 1:
        return len(source)
    dp = [0] * (len(source) + 1)
    dp[0], dp[1] = 1, 1
    dp[2] = 1 + (1 if source[:2] in encode else 0)
    for i in range(3, len(dp)):
        for j in range(3):
            k = i - j - 1
            if source[k:i] in encode:
                dp[i] += dp[k]
    return dp[-1] % 2**32

print(solve(source))