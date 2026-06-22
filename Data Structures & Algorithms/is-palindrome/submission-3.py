class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        r = len(s)-1
        l = 0
        while( l < r):
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[r] == s[l]:
                l+=1
                r-=1
            else:
                return False        
        return True