class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        has = {}
        for a in s:
            has[a] = has.get(a, 0) + 1
        print(has)
        for a in t:
            has[a] = has.get(a, 0) - 1
        print(has)
        return not any(has.values())