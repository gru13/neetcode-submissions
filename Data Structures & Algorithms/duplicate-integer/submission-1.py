class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for a in nums:
            if a in visited:
                return True
            visited.add(a)
        return False