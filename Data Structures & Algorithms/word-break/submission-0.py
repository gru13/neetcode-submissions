class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for word in wordDict:
                if len(word) > i:
                    continue
                if word == s[i-len(word):i]:
                    dp[i] = dp[i] or dp[i-len(word)]
                    print(i, word, )
        return dp[-1]