"""
    暴力串匹配.
"""


def str_match(source, pattern):
    if len(source) < len(pattern):
        return -1
    index = -1
    for i in range(0, len(source)-len(pattern)+1):
        tmp = i
        index = i
        for c in pattern:
            if source[tmp] != c:
                index = -1
                break
            tmp += 1
        if index != -1:
            break
    return index


if __name__ == "__main__":
    source = "aaaaaaaaaabcc"
    pattern = "bc"
    index = str_match(source, pattern)

    print(source)
    print(pattern)
    print(f"str_match => {index} => {source[index:]}")
