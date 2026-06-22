from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        window = Counter()
        left = 0
        word = ""        
        for right in range(len(s)):
            window[s[right]] += 1
            while window >= tc:
                cur_word = s[left:right+1]
                word = cur_word if len(word) >= len(cur_word) or word == "" else word    
                window[s[left]] -= 1
                left += 1
                if window < tc:
                        break
                    
        return word