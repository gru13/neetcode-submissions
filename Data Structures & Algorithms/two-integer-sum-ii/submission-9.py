class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return  [1,2]
        i = 0
        j = len(numbers)-1
        while i < j:
            cur_sum = numbers[i]+numbers[j]
            if cur_sum == target:
                break
            elif cur_sum < target:
                i+=1
            else:
                j-=1
        return [i+1,j+1]