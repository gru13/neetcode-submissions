class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for (i,a) in enumerate(nums):

            if target - a in hs.keys():
                return [hs[target-a], i]
            hs[a] = i

        return [-1,-1]