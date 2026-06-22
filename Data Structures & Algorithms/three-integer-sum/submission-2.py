from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            cur_target = 0 - nums[i]
            d = {}
            for j in range(len(nums)):
                if j == i:
                    continue
                if cur_target - nums[j] in d:
                    a = nums[i]
                    b = nums[j]
                    c = cur_target - nums[j]
                    if a > b: a,b = b,a
                    if a > c: a,c = c,a
                    if b > c: b,c = c,b
                    result.add((a,b,c))
                d[nums[j]] = j
        return list(result)