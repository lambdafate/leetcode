def readToInt():
    return [int(n) for n in input().split()]

def check(cards):
    if not cards:
        return True
    # a == b == c
    if cards[0] == cards[1] == cards[2] and check(cards[3:]):
        return True
    # a b c 
    i = 1
    while i < len(cards) and cards[i] != cards[0] + 1: i += 1
    j = i + 1
    while j < len(cards) and cards[j] != cards[i] + 1: j += 1
    if i < len(cards) and j < len(cards) and check(cards[1:i] + cards[i+1:j] + cards[j+1:]):
        return True
    return False

def fuck(cards):
    cards.sort()
    used = set()
    for i in range(1, len(cards)):
        if cards[i] != cards[i-1] or cards[i] in used:
            continue
        used.add(cards[i])
        if check(cards[:i-1] + cards[i+1:]):
            return True
    return False

def solve(cards):
    leftcards = [4] * 10
    for card in cards:
        leftcards[card] -= 1
    ans = []
    for i in range(1, 10):
        if leftcards[i] > 0 and fuck(cards + [i]):
            ans.append(i)
    return ans
            


if __name__ == "__main__":
    cards = readToInt()
    ans = solve(cards)    
    if ans:
        print(ans[0], end="")
        for i in range(1, len(ans)):
            print(f" {ans[i]}", end="")
    else:
        print(0)