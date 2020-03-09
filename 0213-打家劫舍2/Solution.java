// 不能同时打劫第一家和最后一家哦！！！
class Solution {
    public int rob(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        if(nums.length == 1){
            return nums[0];
        }
        return Math.max(fuck(nums, 0, nums.length-2), fuck(nums, 1, nums.length-1));
    }

    private int fuck(int[] nums, int begin, int end){
        int[] dp = new int[end-begin+1];
        dp[0] = nums[begin];
        if(end>begin){
            dp[1] = Math.max(nums[begin], nums[begin+1]);
        }
        for(int i=begin+2; i<=end; i++){
            dp[i-begin] = Math.max(nums[i]+dp[i-begin-2], dp[i-begin-1]);
        }
        return dp[dp.length-1];
    }
}