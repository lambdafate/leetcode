def solve(s):
    chars = list(s)
    i = 0
    while i < len(chars) - 2:
        if chars[i] != chars[i+1]:
            i += 1
            continue
        if chars[i] == chars[i+2]:
            chars.pop(i + 2)
            continue
        if i + 3 < len(chars) and chars[i + 2] == chars[i + 3]:
            chars.pop(i + 3)
        else:
            i += 1
    return "".join(chars)

if __name__ == "__main__":
    output = []
    for _ in range(int(input())):
        s = input()
        output.append(solve(s))
    for s in output:
        print(s)

