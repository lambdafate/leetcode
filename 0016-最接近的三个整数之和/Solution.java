import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int res = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.length-2; i++) {
            int left=i+1, right=nums.length-1;
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == target){
                    return sum;
                }else if(sum < target){
                    left++;
                }else{
                    right--;
                }
                res = Math.abs(sum-target)<Math.abs(res-target)? sum: res;
            }
        }
        return res;
    }
}