class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rec(lst: list[int], low:int, high:int, target:int):
            if high < low:
                return -1
            mid = (low + high)//2
            if lst[mid] == target:
                return mid
            if lst[mid] > target:
                return rec(lst,low,mid-1,target)
            if lst[mid] < target:
                return rec(lst,mid+1,high,target)
        return rec(nums, 0, len(nums)-1, target)