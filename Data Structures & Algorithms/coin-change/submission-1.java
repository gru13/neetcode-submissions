class Solution {
    Integer dp[];

    public int helper(int[] coins, int amount){
        if(amount == 0){
            return 0;
        }
        if(amount < 0){
            return -1;
        }
        if(dp[amount] != null){
            return dp[amount];
        }
        int min = Integer.MAX_VALUE;
        for(int coin: coins){
            int current = helper(coins, amount - coin);
            if(current == -1){
                continue;
            }
            min = Math.min(min, current + 1);
        }
        if(min == Integer.MAX_VALUE){min = -1;}
        dp[amount] = min ;
        return min;
    }

    public int coinChange(int[] coins, int amount) {
        dp = new Integer[amount+1];
        return helper(coins, amount);
    }
}
