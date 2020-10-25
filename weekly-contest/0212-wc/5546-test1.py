class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        if not releaseTimes or not keysPressed:
            return None
        key, time = None, 0
        for i, k in enumerate(keysPressed):
            curr = releaseTimes[i]
            if i > 0:
                curr -= releaseTimes[i-1]
            if key is None or time < curr or (time == curr and key < k):
                key, time = k, curr
        return key
