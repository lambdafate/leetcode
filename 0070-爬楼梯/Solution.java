// 爬楼梯, 一次可以爬一阶或两阶
class Solution {
    public int climbStairs(int n) {
        if(n <= 2){
            return n;
        }
        // dp[i]代表从0到i的所有爬法
        int[] dp = new int[n];
        dp[0] = 1;
        dp[1] = 2;
        for(int i=2; i<n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n-1];
    }
}