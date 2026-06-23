class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1,]
        for a in nums[:-1]:
            prefix.append(prefix[-1]*a)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            cur_i = nums[i]
            nums[i] = prefix[i]*postfix
            postfix *= cur_i   
        return nums