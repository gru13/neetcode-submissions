from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2c = Counter(s2[:len(s1)])
        s1c = Counter(s1)
        if s1c == s2c : return True
        for i in range(len(s1) , len(s2)):
            s2c[s2[i]] += 1
            s2c[s2[i-len(s1)]] -= 1
            if s1c == s2c:
                return True
        return False