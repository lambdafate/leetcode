def solve(v1, v2):
    v1 = v1.split(".")
    v2 = v2.split(".")
    i, j = 0, 0
    while i < len(v1) or j < len(v2):
        n1 = int(v1[i]) if i < len(v1) else 0
        n2 = int(v2[j]) if j < len(v2) else 0
        if n1 != n2:
            return n1 < n2
        i += 1
        j += 1
    return False

ans = []
for _ in range(int(input())):
    line = input().strip().split()
    if solve(line[0], line[1]):
        ans.append("true")
    else:
        ans.append("false")
for n in ans:
    print(n)
