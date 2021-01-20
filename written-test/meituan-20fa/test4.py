s = input()

def solve(s):
    if not s: return [0]
    ans = []
    i = 0
    while i < len(s):
        j, k = i, i
        while j <= k:
            index = len(s) - 1
            while index > j and s[index] != s[j]: index -= 1
            k = max(k, index)
            j += 1
        ans.append(k - i + 1)
        i = k + 1
    return ans

ans = solve(s)
for n in ans:
    print(f"{n}", end=" ")