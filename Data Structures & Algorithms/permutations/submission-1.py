class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        tracker = [False for _ in range(len(nums))]
        def backtrack(visited):
            if all(tracker):
                if visited not in result:
                    result.append(visited[:])
                return
            for (i,n) in enumerate(nums) :
                if tracker[i]:
                    continue
                tracker[i] = True
                visited.append(n)
                backtrack(visited)
                visited.pop()
                tracker[i] = False

        backtrack([])
        return result