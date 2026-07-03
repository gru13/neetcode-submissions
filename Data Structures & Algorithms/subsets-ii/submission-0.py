class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False for _ in range(len(nums))]
        seen = set()
        def backtrack(cur):
            if tuple(sorted(cur)) in seen:
                return 
            
            result.append(cur.copy())
            seen.add(tuple(sorted(cur)))

            for (i, a) in enumerate(nums):
                if visited[i]:
                    continue
                visited[i] = True
                cur.append(a)
                backtrack(cur)
                cur.pop()
                visited[i] = False

        backtrack([])

        return result