class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = {}
        lft = 0
        max_len = 1
        for ryt in range(len(s)):
            if s[ryt] in seen:
                lft = max(lft, seen[s[ryt]] + 1)
            seen[s[ryt]] = ryt
            max_len = max(max_len, ryt-lft+1)
        return max_len