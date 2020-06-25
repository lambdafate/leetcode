"""
    KMP串匹配算法
"""


def NEXT(pattern):
    nexts = []
    for index, char in enumerate(pattern):
        if index <= 1:
            nexts.append(index-1)
            continue
        nexts.append(0)
        for k in range(index-1, 0, -1):
            if pattern[0:k] == pattern[index-k:index]:
                nexts[index] = k
                break
    return nexts


def KMP(source, pattern):
    if len(source) < len(pattern):
        return -1
    nexts = NEXT(pattern)
    i, j = 0, 0
    while i < len(source) and j < len(pattern):
        if source[i] == pattern[j]:
            i, j = i+1, j+1
            continue
        j = nexts[j]
        if j == -1:
            i, j = i+1, 0

    if j == len(pattern):
        return i - j
    return -1



if __name__ == "__main__":
    source = "aaaaaaaaaabcc"
    pattern = "bc"
    index = KMP(source, pattern)

    print(source)
    print(pattern)
    print(f"KMP => {index} => {source[index:]}")
