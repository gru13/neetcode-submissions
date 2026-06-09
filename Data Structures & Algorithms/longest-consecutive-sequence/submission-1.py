class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for a in nums:
            if a - 1 not in nums:
                leng = 0
                while a + leng in nums:
                    leng += 1
                longest = max(leng, longest)
        return longest