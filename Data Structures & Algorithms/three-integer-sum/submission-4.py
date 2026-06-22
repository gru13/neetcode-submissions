class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            d = {}
            for j in range(len(nums)):
                if j == i:
                    continue
                if -(nums[i] + nums[j]) in d:
                    a = nums[i]
                    b = nums[j]
                    c = -(nums[i] + nums[j])
                    if a > b: a,b = b,a
                    if a > c: a,c = c,a
                    if b > c: b,c = c,b
                    result.add((a,b,c))
                d[nums[j]] = j
        return list(result)