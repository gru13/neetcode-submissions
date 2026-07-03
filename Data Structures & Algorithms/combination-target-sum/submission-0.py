class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(curSum, elements):
            if curSum == 0:
                e = sorted(elements[:])
                if e not in result:
                    result.append(e)
                return
            if curSum < 0:
                return
            for a in nums:
                elements.append(a)
                backtrack(curSum-a, elements)
                elements.pop()

        backtrack(target, [])
        return result