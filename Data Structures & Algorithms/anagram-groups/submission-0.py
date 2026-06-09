from collections import Counter
from itertools import groupby
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = {}
        for a in strs:
            ac = tuple(sorted(Counter(a).items()))
            index[ac] = index.get(ac, []) + [a]
        return list(index.values())