class Solution:
    def climb(self,i, cost, total):
        if i >= len(cost):
            return total;
        else :
            return min(self.climb(i+1, cost, total + cost[i]), self.climb(i+2, cost, total + cost[i]))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.climb(0, cost, 0), self.climb(1, cost, 0))