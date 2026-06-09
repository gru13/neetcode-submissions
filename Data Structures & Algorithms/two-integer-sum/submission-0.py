class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv = dict()
        for i,a in enumerate(nums):
            if target - a in kv.keys():
                return [kv[target - a], i]
            else:
                kv[a] = i
        return -1