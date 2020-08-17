class Solution:
    def permutation(self, s: str) -> List[str]:
        if len(s) < 2:
            return [s]
        norepeat, result = set(), []
        chars = list(s)
        self.backtrace(0, norepeat, result, chars)
        return result

    def backtrace(self, index, norepeat, result, chars):
        if index == len(chars)-1:
            result.append("".join(chars))
            return
        for i in range(index, len(chars)):
            chars[index], chars[i] = chars[i], chars[index]
            tmp = "".join(chars[:index+1])
            if tmp in norepeat:
                chars[index], chars[i] = chars[i], chars[index]
                continue
            norepeat.add(tmp)
            self.backtrace(index+1, norepeat, result, chars)
            chars[index], chars[i] = chars[i], chars[index]
