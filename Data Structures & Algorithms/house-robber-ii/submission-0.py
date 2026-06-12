class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        ## where we start in house index 0 and doesnt include the last house
        nums1 = nums[:-1]
        dp1 = [nums1[0], max(nums1[:2])] 

        for i in range(2, len(nums1)):
            dp1.append(max(nums1[i]+dp1[i-2], dp1[i-1]))


        ## where we start in house index 1 and include the last house 
        nums2 = nums[1:]
        dp2 = [nums2[0], max(nums2[:2])]
        for i in range(2, len(nums2)):
            dp2.append(max(nums2[i]+dp2[i-2], dp2[i-1]))

        return max(dp1[-1], dp2[-1])
