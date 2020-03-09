class Solution {
    public int rob(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        if(nums.length == 1){
            return nums[0];
        }
        // dp[i]: 打劫0~i家所获得的最大利益
        int[] dp = new int[nums.length];
        // dp init
        dp[0] = nums[0];
        dp[1] = Math.max(dp[0], nums[1]);
       
        for(int i=2; i<nums.length; i++){
            dp[i] = Math.max(nums[i]+dp[i-2], dp[i-1]);
        }

        return dp[nums.length-1];

    }
}