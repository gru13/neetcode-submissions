from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        co = defaultdict(int)
        for a in s:
            co[a] += 1
        print(co)
        for b in t:
            if b not in co.keys():
                return False
            co[b] -= 1
        print(co)
        return all([a==0 for a in co.values()])
        