class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        maxL = 0
        l = 0
        r = 1
        count = set(s[l])  
        while r < len(s):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            maxL = max(maxL, len(count))
            r += 1
        return maxL
            
