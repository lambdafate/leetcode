class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        int max = nums[0];
        for(int i = 0; i<nums.length; i++){
            int sum = 0;
            for(int j = i; j<nums.length; j++){
                sum += nums[j];
                if(sum > max){
                    max = sum;
                }
            }
        }
        return max;
        
        
    }
}