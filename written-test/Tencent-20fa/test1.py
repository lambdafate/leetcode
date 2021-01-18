
def solve(s):
    if not s: return s
    i = 0
    while i < len(s) and s[i] != "[": i += 1
    if i >= len(s):
        return s
    j = i + 1
    while j < len(s) and s[j] != "|": j += 1
    length = int(s[i+1:j])
    left = 1
    k = j
    while k < len(s):
        if s[k] == "[":
            left += 1
        elif s[k] == "]":
            left -= 1
        if left == 0: break
        k += 1
    return s[:i] + solve(s[j+1:k]) * length + solve(s[k+1:])


if __name__ == "__main__":
    s = input()
    print(solve(s))