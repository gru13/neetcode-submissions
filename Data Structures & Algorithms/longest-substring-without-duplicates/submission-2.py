class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        r = 1
        count = set(s[0])
        maxL = 0 
        while r < len(s):
            if s[r] in count:
                maxL = max(maxL, len(count))
                l = l + 1
                count = set(s[l])
                r = l
            else:
                count.add(s[r])
            r += 1
        maxL = max(maxL, len(count))
        return maxL