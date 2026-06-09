class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxV = 0
        while i < j:
            v = (j-i)*min(heights[i], heights[j])
            maxV = max(v, maxV)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxV