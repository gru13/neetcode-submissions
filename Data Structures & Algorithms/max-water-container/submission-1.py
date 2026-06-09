class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftP, rightP = 0, len(heights)-1
        maxV = 0
        while leftP < rightP:
            width = rightP - leftP 
            height = min(heights[leftP] , heights[rightP])
            maxV = max(maxV, width*height)
            if heights[leftP] < heights[rightP]:
                leftP += 1
            else:
                rightP -= 1

        return maxV 