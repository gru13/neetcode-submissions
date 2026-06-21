from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums).items()
        sorted_nc = sorted(nums_counter, key=lambda x : x[1])
        return [a for (a,b) in list(sorted_nc)[-k:]]    