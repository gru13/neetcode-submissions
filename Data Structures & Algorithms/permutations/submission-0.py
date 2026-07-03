class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(visited):
            if len(visited) == len(nums):
                if visited not in result:
                    result.append(visited[:])
                return
            for n in nums :
                if n in visited:
                    continue
                visited.append(n)
                backtrack(visited)
                visited.pop()
        backtrack([])
        return result