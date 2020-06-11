public class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount == 0){
            return 0;
        }
        int dp[] = new int[amount+1];
        dp[0] = 0;
        for (int i = 1; i < dp.length; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        for (int i = 1; i < dp.length; i++) {
            for (int coin : coins) {
                int index = i-coin;
                if(index >= 0 && dp[index] != -1){
                    dp[i] = Math.min(dp[i], 1+dp[index]);
                }
            }
            dp[i] = dp[i] == Integer.MAX_VALUE ? -1: dp[i];
        }
        return dp[amount];
    }
}