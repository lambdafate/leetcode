class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length < 2) {
            return 0;
        }
        // dp[i] 代表截止到i天所得最大利润
        // dp[i] = max(dp[i-1], prices[i]-minprice)
        int minprice = prices[0];
        int[] dp = new int[prices.length];
        dp[0] = 0;
        for(int i=1; i<prices.length; i++){
            // 决定是否在第i天卖出来计算截止到该天的最大利润
            dp[i] = Math.max(dp[i-1], prices[i]-minprice);
            // 更新minprice
            minprice = Math.min(minprice, prices[i]);
        }

        return dp[prices.length-1];
    }
}