class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numa = [0]
        # ls = [[]]
        index = 0
        
        nums.sort()

        for i in range(len(nums)):
            numa[index] += 1
            
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                numa[index] -= 1 
            
            # ls[index].append(nums[i]) 
            
            if i + 1 < len(nums) and nums[i+1] != nums[i]  and nums[i+1] != nums[i] + 1:
                index += 1
                # ls.append([])
                numa.append(0)  

        # print(ls)
        return max(numa)