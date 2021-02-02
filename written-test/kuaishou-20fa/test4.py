def solve(s1, s2):
    ans = []
    i, j = 0, 0
    while i + 4 < len(s1) and j < len(s2):
        for _ in range(4):
            ans.append(s1[i])
            i += 1
        ans.append(s2[j])
        j += 1
    ans += s1[i:] + s2[j:]
    return ans

s1 = input().split()
s2 = input().split()
for n in solve(s1, s2):
    print(n, end=" ")
