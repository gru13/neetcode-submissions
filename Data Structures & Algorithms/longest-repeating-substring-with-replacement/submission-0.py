from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_d = 0
        max_f = 0
        for rigth in range(len(s)):
            # move left
            freq[s[rigth]] += 1
            if freq[s[rigth]] > max_f:
                max_f = freq[s[rigth]]

            if (rigth - left + 1) - max_f > k:
                freq[s[left]] -= 1
                left += 1
            max_d = max(rigth-left + 1, max_d)

        return max_d