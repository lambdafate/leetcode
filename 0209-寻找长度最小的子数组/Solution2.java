// 暴力法
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if(sum >= s){
                    res = Math.min(res, j-i+1);
                    break;
                }
            }
        }
        return res == Integer.MAX_VALUE ? 0: res; 
    }
}