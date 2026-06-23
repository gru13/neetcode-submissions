from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            a =  "".join(sorted(list(s)))
            result[a].append(s)

        return list(result.values())