class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = []
        for a in nums:
            if a not in t:
                t.append(a)
            else:
                return True
        return False
        