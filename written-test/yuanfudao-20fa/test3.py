def solve(s):
    if not s:
        return s
    i = 0
    while i < len(s) and s[i] != "(" and not s[i].isdigit(): i += 1
    if i >= len(s):
        return s
    if s[i].isdigit():
        j = i
        while i < len(s) and s[i].isdigit(): i += 1
        return s[:j - 1] + s[j - 1] * int(s[j:i]) + solve(s[i:])
    left = 1
    j = i + 1
    while j < len(s):
        if s[j] == "(":
            left += 1
        elif s[j] == ")":
            left -= 1
            if left == 0: break
        j += 1
    k = j + 1
    while k < len(s) and s[k].isdigit(): k += 1
    return s[:i] + solve(s[i+1:j]) * int(s[j+1:k]) + solve(s[k:])


output = []
for _ in range(int(input())):
    s = input()
    output.append(solve(s))
for s in output:
    print(s)

# print(solve("E(((AB)2C)2((DC)2)3)2E"))
