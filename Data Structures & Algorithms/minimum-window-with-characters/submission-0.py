from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        window = Counter()
        left = 0
        word = ""        
        for right in range(len(s)):
            window[s[right]] += 1
            if window >= tc:
                print(window , tc, s[left:right+1])   
                word = s[left:right+1] if len(word) >= len(s[left:right+1]) or word == "" else word
                while left < right:
                    window[s[left]] -= 1
                    left += 1
                    if window >= tc:
                        word = s[left:right+1] if len(word) >= len(s[left:right+1]) else word
                    else:
                        break
                    
        return word