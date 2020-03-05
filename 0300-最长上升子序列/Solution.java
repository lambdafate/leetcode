class Solution {
    public int lengthOfLIS(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        int[] dp = new int[nums.length];
        dp[0] = 1;
        int maxlength = 1;
        for(int i=1; i<nums.length; i++){
            // 计算所有到该节点的最大距离
            dp[i] = 0;
            for(int j=0; j<i; j++){
                if(nums[j] < nums[i] && dp[j] > dp[i]){
                    dp[i] = dp[j];
                }
            }
            dp[i] += 1;
            if(maxlength < dp[i]){
                maxlength = dp[i];
            }
        }
        return maxlength;
    }
}