class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        lft = 0
        max_len = 0
        for ryt in range(len(s)):
            if s[ryt] in seen:
                lft = max(lft, seen[s[ryt]] + 1)
            seen[s[ryt]] = ryt
            max_len = max(max_len, ryt-lft+1)
        return max_len