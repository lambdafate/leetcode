// 使用动态规划, fuck it
class SolutionDp {
    public int maxSubArray(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        // dp中的每一项代表从前面某一项到该项的最大连续和
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        int res = dp[0];
        for(int i=1; i<nums.length; i++){
            dp[i] = nums[i];
            if(dp[i-1] > 0){
                dp[i] += dp[i-1];
            }
            if(dp[i] > res){
                res = dp[i];
            }
        }
        return res;
    }
}